from flask_restful import Resource, reqparse,abort
from apps.models.models import User
from sqlalchemy import or_
from apps.exts import cache
from .common import HOME_TOKEN_PREFIX

parser = reqparse.RequestParser()
parser.add_argument('contact', required=True, help='username or email or phone error')
parser.add_argument('password', required=True, help='password error')


class UserLoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        contact = args.get('contact')
        password = args.get('password')
        user_obj = User.query.filter(or_(User.name==contact,User.email==contact,User.phone==contact)).first()
        if not user_obj:
            abort(404,message='用户不存在')
        if not user_obj.check_pwd(password):
            abort(404,message='密码错误')
        token = HOME_TOKEN_PREFIX + user_obj.uuid
        cache.set(token,user_obj.id)
        data = {
            'status':200,
            'token':token,
            'msg':'success'
        }

        return data