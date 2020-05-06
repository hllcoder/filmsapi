from flask_restful import Resource, fields, marshal_with, marshal
from apps.models.models import User
from apps.exts import db

singel_field = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'face': fields.String,
    'add_time': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singel_field))
}


class AdminMemberResource(Resource):
    @marshal_with(source_field)
    def get(self):
        user_obj = User.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': user_obj
        }
        return data


class AdminMemberDetailResource(Resource):
    def get(self, user_id):
        user_obj = User.query.get(user_id)
        data = {
            'status': 200,
            'msg': 'success',
            'data': marshal(user_obj, singel_field)
        }
        return data

    def delete(self, user_id):
        user_obj = User.query.get(user_id)
        db.session.delete(user_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除会员成功'
        }
        return data
