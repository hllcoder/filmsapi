from flask_restful import Resource, reqparse, marshal_with, fields,marshal
from apps.models.models import Auth
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='name error')
parser.add_argument('url', required=True, help='url error')

singal_field = {
    'id': fields.Integer,
    'name': fields.String,
    'url': fields.String
}

resource_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class AdminAuthResource(Resource):
    @marshal_with(resource_field)
    def get(self):
        auth_obj = Auth.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': auth_obj
        }
        return data

    def post(self):
        args = parser.parse_args()
        name = args.get('name')
        url = args.get('url')
        auth_obj = Auth(
            name=name,
            url=url
        )
        db.session.add(auth_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '创建权限成功'
        }
        return data


class AdminAuthDetailResource(Resource):
    def get(self, auth_id):
        auth_obj = Auth.query.get(auth_id)
        data = {
            'status': 200,
            'msg': 'success',
            'data': marshal(auth_obj,singal_field)
        }
        return data

    def put(self, auth_id):
        auth_obj = Auth.query.get(auth_id)
        args = parser.parse_args()
        name = args.get('name')
        url = args.get('url')
        auth_obj.name = name
        auth_obj.url = url
        db.session.add(auth_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '修改权限成功'
        }
        return data

    def delete(self, auth_id):
        auth_obj = Auth.query.get(auth_id)
        db.session.delete(auth_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除权限记录成功'
        }
        return data
