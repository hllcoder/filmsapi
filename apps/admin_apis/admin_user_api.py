from flask_restful import Resource, reqparse, fields, marshal_with, abort
from apps.models.models import Admin
from werkzeug.security import generate_password_hash
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='name error')
parser.add_argument('pwd', required=True, help='pwd error')
parser.add_argument('role_id', type=int, help='role_id error')

singal_field = {
    'id': fields.Integer,
    'name': fields.String,
    'role': fields.Nested({'name': fields.String})
}

resoure_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class AdminUserResource(Resource):
    @marshal_with(resoure_field)
    def get(self):
        admin_obj = Admin.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': admin_obj
        }
        return data

    def post(self):
        args = parser.parse_args()
        name = args.get('name')
        pwd = args.get('pwd')
        role_id = args.get('role_id')
        ad_obj = Admin.query.filter_by(name=name).first()
        if ad_obj:
            abort(404, message='用户已存在')
        pwd_hash = generate_password_hash(pwd)
        admin_obj = Admin(
            name=name,
            pwd=pwd_hash,
            role_id=role_id
        )
        db.session.add(admin_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '创建管理员成功'
        }
        return data
