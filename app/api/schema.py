from datetime import datetime, timedelta

from voluptuous import Optional, Schema


def Date(fmt='%Y-%m-%d'):
    return lambda v: datetime.strptime(v, fmt)


def StringList(v):
    return tuple(v.split(','))


default_price_schema = Schema({
    Optional('nodes', default=('BEN2201', 'HAY2201', 'INV2201', 'ISL2201', 'OTA2201')): StringList,
    Optional('start_date', default=datetime.today().date() - timedelta(days=30)): Date(),
    Optional('end_date', default=datetime.today().date()): Date()
})
