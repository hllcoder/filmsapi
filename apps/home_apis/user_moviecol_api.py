from flask_restful import Resource, fields, marshal_with, abort
from flask import g
from apps.models.models import Moviecol
from apps.utils import decorate_fuc
from apps.exts import db

movie_field = {
    'title': fields.String,
    'info': fields.String,
    'url': fields.String,
    'logo': fields.String
}

singal_field = {
    'id': fields.Integer,
    'movie': fields.Nested(movie_field)
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class UserMovieColResource(Resource):
    @decorate_fuc
    @marshal_with(source_field)
    def get(self):
        user_obj = g.user
        moviecol_obj = Moviecol.query.filter_by(user_id=user_obj.id)
        data = {
            'status': 200,
            'msg': '获取电影收藏成功',
            'data': moviecol_obj
        }
        return data


class UserMovieColDetailResource(Resource):
    @decorate_fuc
    def post(self, movie_id):
        user_obj = g.user
        col_obj = Moviecol.query.filter_by(movie_id=movie_id, user_id=user_obj.id).first()
        if col_obj:
            abort(404, message='该电影已收藏')
        moviecol_obj = Moviecol(
            movie_id=movie_id,
            user_id=user_obj.id
        )
        db.session.add(moviecol_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '电影收藏成功'
        }
        return data

    @decorate_fuc
    def delete(self, movie_id):
        user_obj = g.user
        moviecol_obj = Moviecol.query.filter_by(movie_id=movie_id, user_id=user_obj.id)
        db.session.delete(moviecol_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '取消电影收藏成功'
        }
        return data
