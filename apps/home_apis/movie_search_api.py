from flask_restful import Resource, fields, marshal_with
from apps.models.models import Movie
from flask import request

singal_field = {
    'id': fields.Integer,
    'logo': fields.String,
    'url': fields.String,
    'info': fields.String,
    'title':fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class MovieSearchResource(Resource):
    @marshal_with(source_field)
    def get(self):
        name = request.args.get('name')
        movie_obj = Movie.query.filter(Movie.title.ilike('%' + name + '%'))
        data = {
            'status': 200,
            'msg': '搜索电影成功',
            'data': movie_obj
        }
        return data
