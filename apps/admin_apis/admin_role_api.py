from flask_restful import Resource, reqparse, marshal_with, fields, marshal
from apps.models.models import Role
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='name error')
parser.add_argument('auths', required=True, help='url error')

singal_field = {
    'id': fields.Integer,
    'name': fields.String,
    'auths': fields.String,
    'add_time': fields.String
}

resource_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class AdminRoleResource(Resource):
    @marshal_with(resource_field)
    def get(self):
        role_obj = Role.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': role_obj
        }
        return data

    def post(self):
        args = parser.parse_args()
        name = args.get('name')
        auths = args.get('auths')
        role_obj = Role(
            name=name,
            auths=auths
        )
        db.session.add(role_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '创建角色成功'
        }
        return data


class AdminRoleDetailResource(Resource):
    def get(self, role_id):
        role_obj = Role.query.get(role_id)
        data = {
            'status': 200,
            'msg': 'success',
            'data': marshal(role_obj, singal_field)
        }
        return data

    def put(self, role_id):
        role_obj = Role.query.get(role_id)
        args = parser.parse_args()
        name = args.get('name')
        auths = args.get('auths')
        role_obj.name = name
        role_obj.auths = auths
        db.session.add(role_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '修改角色成功'
        }
        return data

    def delete(self, role_id):
        role_obj = Role.query.get(role_id)
        db.session.delete(role_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除角色记录成功'
        }
        return data
