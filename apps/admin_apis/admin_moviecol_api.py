from flask_restful import Resource, fields, marshal_with
from apps.models.models import Moviecol
from apps.exts import db

singal_field = {
    'id': fields.Integer,
    'movie': fields.Nested({'title': fields.String}),
    'user': fields.Nested({'name': fields.String}),
    'add_time': fields.String
}

resource_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class AdminMovieColResource(Resource):
    @marshal_with(resource_field)
    def get(self):
        moviecol_obj = Moviecol.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': moviecol_obj
        }
        return data


class AdminMovieColDetailResource(Resource):
    def get(self, moviecol_id):
        moviecol_obj = Moviecol.query.get(moviecol_id)
        db.session.delete(moviecol_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除电影收藏成功'
        }
        return data
