from flask_restful import Resource, fields, marshal_with
from apps.models.models import OpLog, AdminLog, UserLog

singal_field = {
    'id': fields.Integer,
    'admin': fields.Nested({'name': fields.String}),
    'ip': fields.String,
    'reason': fields.String,
    'add_time': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}

admin_field = {
    'id': fields.Integer,
    'admin': fields.Nested({'name': fields.String}),
    'ip': fields.String,
    'add_time': fields.String
}

adminlog_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(admin_field))
}

user_field = {
    'id': fields.Integer,
    'user': fields.Nested({'name': fields.String}),
    'ip': fields.String,
    'add_time': fields.String
}

userlog_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_field))
}


class AdminOpLogResource(Resource):
    @marshal_with(source_field)
    def get(self):
        oplog_obj = OpLog.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': oplog_obj
        }
        return data


class AdminLogResource(Resource):
    @marshal_with(adminlog_field)
    def get(self):
        adminlog_obj = AdminLog.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': adminlog_obj
        }
        return data


class UserLogResource(Resource):
    @marshal_with(userlog_field)
    def get(self):
        user_log_obj = UserLog.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': user_log_obj
        }
        return data
