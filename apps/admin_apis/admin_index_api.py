from flask_restful import Resource
from flask import g
from .commons import decorate


class AdminIndexResource(Resource):
    @decorate
    def get(self):
        user_obj = g.user
        data = {
            'status': 200,
            'msg': 'success',
            'username': user_obj.name
        }
        return data
