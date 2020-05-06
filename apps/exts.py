from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()


def init_ext(app):
    db.init_app(app=app)
    cache.init_app(app)
