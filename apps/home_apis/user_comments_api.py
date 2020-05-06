from flask_restful import Resource, fields, marshal_with, reqparse
from apps.models.models import Comment
from apps.utils import decorate_fuc
from flask import g
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('movie_id', type=int, required=True, help='movie_id error')
parser.add_argument('content', required=True, help='content error')

user_field = {
    'id': fields.Integer,
    'name': fields.String,
    'face': fields.String
}

singal_field = {
    'id': fields.Integer,
    'content': fields.String,
    'movie': fields.Nested({'title': fields.String}),
    'user': fields.Nested(user_field)
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class UserCommentResource(Resource):
    @decorate_fuc
    @marshal_with(source_field)
    def get(self):
        user_obj = g.user
        comment_obj = Comment.query.filter(Comment.user_id == user_obj.id)
        data = {
            'status': 200,
            'msg': '获取评论成功',
            'data': comment_obj
        }
        return data

    @decorate_fuc
    def post(self):
        args = parser.parse_args()
        movie_id = args.get('movie_id')
        content = args.get('content')
        user_obj = g.user
        comment_obj = Comment(
            movie_id=movie_id,
            user_id=user_obj.id,
            content=content
        )
        db.session.add(comment_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '添加电影评论成功'
        }
        return data
