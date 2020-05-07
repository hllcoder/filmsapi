from flask_restful import Resource, reqparse,abort
from apps.models.models import Admin
from apps.exts import cache
from .commons import ADMIN_TOKEN_PREFIX
import uuid

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help='username error')
parser.add_argument('password', required=True, help='password error')


class AdminUserLoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        user_obj = Admin.query.filter_by(name=username).first()
        if not user_obj:
            abort(400,message='用户名错误')
        if not user_obj.check_pwd(password):
            abort(400,message='密码错误')
        token = ADMIN_TOKEN_PREFIX + str(uuid.uuid4().hex)
        cache.set(token,user_obj.id)
        data = {
            'status':200,
            'token':token,
            'msg':'success'
        }

        return data
