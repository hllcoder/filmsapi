from flask_restful import Resource, reqparse,abort
from apps.models.models import User
from werkzeug.security import generate_password_hash
from apps.exts import db
import uuid

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help='name error')
parser.add_argument('email', required=True,help='email error')
parser.add_argument('phone', required=True, help='phone error')
parser.add_argument('password', required=True, help='password error')



class UserRegisterResource(Resource):
    def post(self):
        args = parser.parse_args()
        name = args.get('name')
        pwd = args.get('password')
        email = args.get('email')
        phone = args.get('phone')
        user_obj = User.query.filter_by(name=name).first()
        if user_obj:
            abort(404,message='用户名已存在')
        phone_obj = User.query.filter_by(phone=phone).first()
        if phone_obj:
            abort(404,message='该手机号已注册')
        email_obj = User.query.filter_by(email=email).first()
        if email_obj:
            abort(404,message='该邮箱已注册')
        pwd_hash = generate_password_hash(pwd)
        user = User(
            name=name,
            pwd=pwd_hash,
            email=email,
            phone=phone,
            uuid=uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        data = {
            'status':201,
            'msg':'success'
        }
        return data
