from StringIO import StringIO

from flask import Response
from sqlalchemy import text

from ohm.extensions import db


def _copy_sql(sql, params, buf):
    conn = db.engine.raw_connection()
    c = conn.cursor()
    sql = c.mogrify(sql, params)
    sql = "COPY ({}) TO STDOUT WITH CSV HEADER".format(sql)
    c.copy_expert(sql, buf)


def make_csv_response(sql, params):
    """
    `sql` is a SQLAlchemy parameterized string. Compile it to the postgres dialect so we can use the
    raw connection and copy_expert.
    """

    sql = str(text(sql).compile(dialect=db.session.bind.dialect))

    buf = StringIO()
    _copy_sql(sql, params, buf)

    return Response(buf.getvalue(), status=200, mimetype='text/csv')
