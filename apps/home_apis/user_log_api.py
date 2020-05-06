from flask_restful import Resource, fields, marshal_with
from apps.models.models import UserLog
from apps.utils import decorate_fuc
from flask import g

singal_field = {
    'id': fields.Integer,
    'ip': fields.String,
    'user_id': fields.Integer,
    'add_time': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class UserLogDetailResource(Resource):
    @decorate_fuc
    @marshal_with(source_field)
    def get(self):
        user_obj = g.user
        user_log_obj = UserLog.query.filter(UserLog.user_id == user_obj.id)
        data = {
            'status': 200,
            'msg': '获取登录日志成功',
            'data': user_log_obj
        }
        return data
