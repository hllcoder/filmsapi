from flask_restful import Resource, fields, marshal_with
from apps.models.models import Movie, Comment

movie_field = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String,
    'info': fields.String,
    'star': fields.Integer,
    'playnum': fields.Integer,
    'commentnum': fields.Integer,
    'tag': fields.Nested({'name': fields.String}),
    'area': fields.String,
    'release_time': fields.String,
    'length': fields.String
}

user_field = {
    'name': fields.String,
    'face': fields.String
}

comment_field = {
    'id': fields.Integer,
    'content': fields.String,
    'user': fields.Nested(user_field),
    'add_time': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'movie_data': fields.Nested(movie_field),
    'comment_data': fields.List(fields.Nested(comment_field))
}


class MoviePlayResource(Resource):
    @marshal_with(source_field)
    def get(self, movie_id):
        movie_obj = Movie.query.get(movie_id)
        comment_obj = Comment.query.filter_by(movie_id=movie_id).order_by(Comment.add_time.desc())
        data = {
            'status': 200,
            'msg': '获取数据成功',
            'movie_data': movie_obj,
            'comment_data': comment_obj
        }
        return data
