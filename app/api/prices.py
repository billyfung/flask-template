from itertools import groupby

from flask import request
from app.extensions import db
from app.decorators import dataschema
from app.api import ApiResult, ApiException
from app.api.utils import make_csv_response
from app.api.schema import default_price_schema

from . import api


def _spot_price_latest_chartjs(rows):
    data = {'datasets': []}

    for k, g in groupby(rows, key=lambda x: x.node):
        g = list(g)
        data['datasets'].append({
            'label': k,
            'data': [x.price for x in g]
        })

    data['labels'] = [x.nztimestamp.isoformat() for x in g]
    data['trading_periods'] = [[x.nzdate.isoformat(), x.tp] for x in g]

    return data


@api.route('/spot_price_latest')
@dataschema(default_price_schema)
def spot_price_latest(nodes, start_date, end_date):
    sql = """
    select
        node,
        nzdate,
        tp,
        price
    from prices
    where
        node in :nodes
    and nzdate between :start_date and :end_date
    order by node, nzdate, tp
    """

    params = {
        'nodes': nodes,
        'start_date': start_date,
        'end_date': end_date
    }

    try:
        if request.headers.get('Accept') == 'application/json':
            rows = db.session.execute(sql, params).fetchall()
            data = _spot_price_latest_chartjs(rows)
            return ApiResult(data)
        # Default to return csv response
        return make_csv_response(sql, params)
    except BaseException as e:
        raise ApiException(str(e))
