from apps.exts import cache
from functools import wraps
from apps.home_apis.common import HOME_TOKEN_PREFIX
from apps.models.models import Admin, User
from flask import request,g
from flask_restful import abort
import os,uuid
from datetime import datetime



def change_filename(filename):
    name = os.path.splitext(filename)
    new_filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + name[-1]
    return new_filename



ADMIN_TOKEN_PREFIX = 'admin_'

def decorate(func):
    @wraps(func)
    def inner(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            abort(404, message='请提供token令牌')
        user_id = cache.get(token)
        if not user_id:
            abort(404, message='token令牌已过期')
        if token.startswith(HOME_TOKEN_PREFIX):
            user_obj = User.query.get(user_id)
        if token.startswith(ADMIN_TOKEN_PREFIX):
            user_obj = Admin.query.get(user_id)
        g.user = user_obj
        response = func(*args, **kwargs)
        return response

    return inner