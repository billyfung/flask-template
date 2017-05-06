from flask import Flask, Response, Blueprint, json


api = Blueprint('api', __name__, url_prefix='/api')


class ApiFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


class ApiResult:
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(
            json.dumps(self.value),
            status=self.status,
            mimetype='application/json'
        )


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message}, status=self.status)

# import the api routes here
from .prices import *
