from flask_restful import Resource, reqparse, fields, marshal
from flask import g, request
from apps.exts import db
from apps.utils import decorate_fuc, change_filename
from apps.models.models import User
from apps.settings import BASE_PATH, UPLOAD_FOLDER
import os

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'info': fields.String,
    'face': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='username error')
parser.add_argument('email', required=True, help='email error')
parser.add_argument('phone', required=True, help='phone error')
parser.add_argument('info', help='info error')


class UserResource(Resource):
    @decorate_fuc
    def get(self):
        data = {
            'status': 200,
            'msg': 'success',
            'data': marshal(g.user, resource_fields)
        }
        return data


class UserDetailResource(Resource):

    def put(self, user_id):
        args = parser.parse_args()
        user_obj = User.query.get(user_id)
        user_obj.name = args.get('name')
        user_obj.email = args.get('email')
        user_obj.phone = args.get('phone')
        user_obj.info = args.get('info')
        file = request.files['face']
        filename = file.filename
        new_filename = change_filename(filename)
        real_path = os.path.join(os.path.join(BASE_PATH, UPLOAD_FOLDER), new_filename)
        file.save(real_path)
        user_obj.face = UPLOAD_FOLDER + '/' + new_filename
        db.session.add(user_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': 'success'
        }
        return data
