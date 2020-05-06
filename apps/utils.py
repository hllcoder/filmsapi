import uuid,os
from functools import wraps
from datetime import datetime
from apps.exts import cache
from flask import request, g
from flask_restful import abort
from apps.models.models import User, Admin
from apps.home_apis.common import HOME_TOKEN_PREFIX
from apps.admin_apis.commons import ADMIN_TOKEN_PREFIX


def decorate_fuc(func):
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


def change_filename(filename):
    name = os.path.splitext(filename)
    new_filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + name[-1]
    return new_filename