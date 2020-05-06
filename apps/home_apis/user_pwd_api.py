from flask_restful import Resource,reqparse,abort
from apps.utils import decorate_fuc
from werkzeug.security import generate_password_hash
from flask import g
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('oldpwd',required=True,help='oldpwd error')
parser.add_argument('newpwd',required=True,help='newpwd error')



class UserPwdResource(Resource):
    @decorate_fuc
    def post(self):
        args = parser.parse_args()
        oldpwd = args.get('oldpwd')
        newpwd = args.get('newpwd')
        user_obj = g.user
        if not user_obj.check_pwd(oldpwd):
            abort(404,message='旧密码错误')
        if oldpwd == newpwd:
            abort(404,message='新旧密码不能相同')
        new_pwd = generate_password_hash(newpwd)
        user_obj.pwd = new_pwd
        db.session.add(user_obj)
        db.session.commit()
        data = {
            'status':201,
            'msg':'修改密码成功'
        }
        return data



