from flask import Flask
from apps.home_apis import init_home_api
from apps.admin_apis import init_admin_api
from apps.exts import init_ext
from apps.settings import envs

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_home_api(app=app)
    init_admin_api(app=app)
    init_ext(app)
    return app