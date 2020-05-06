from flask_restful import Resource, fields, marshal_with
from apps.models.models import Movie
from flask import request

movie_field = {
    'id': fields.Integer,
    'logo': fields.String,
    'url': fields.String,
    'star': fields.Integer,
    'title': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'movie_data': fields.List(fields.Nested(movie_field))
}


class HomeIndexResource(Resource):
    @marshal_with(source_field)
    def get(self):
        tag_id = request.args.get('tid', 0)
        star = request.args.get('star', 0)
        time = request.args.get('time', 0)
        play_num = request.args.get('pm', 0)
        comment_num = request.args.get('cm', 0)
        if tag_id:
            movie_obj = Movie.query.filter_by(tag_id=int(tag_id))
        if star:
            movie_obj = Movie.query.filter_by(star=int(star))
        if time:
            movie_obj = Movie.query.order_by(Movie.add_time.desc())
        if play_num:
            if play_num == 1:
                movie_obj = Movie.query.order_by(Movie.playnum.desc())
            else:
                movie_obj = Movie.query.order_by(Movie.playnum.asc())
        if comment_num:
            if comment_num == 1:
                movie_obj = Movie.query.order_by(Movie.comment_num.desc())
            else:
                movie_obj = Movie.query.order_by(Movie.comment_num.asc())
        if not request.args:
            movie_obj = Movie.query.all()
        data = {
            'status': 200,
            'msg': '获取电影资源成功',
            'movie_data': movie_obj
        }
        return data
