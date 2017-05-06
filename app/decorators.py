from functools import update_wrapper

from flask import request
from voluptuous import Invalid

from app.api import ApiException


def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.args.to_dict()))
            except Invalid as e:
                raise ApiException('Invalid data: {} (path "{}")'.format(e.msg, '.'.join(e.path)))
            return f(*args, **kwargs)
        return update_wrapper(new_func, f)
    return decorator
