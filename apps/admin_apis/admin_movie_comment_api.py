from flask_restful import Resource, fields, marshal_with
from apps.models.models import Comment
from apps.exts import db

singal_field = {
    'id': fields.Integer,
    'content': fields.String,
    'add_time': fields.String,
    'movie': fields.Nested({'title': fields.String}),
    'user': fields.Nested({'name': fields.String})
}

source_field = {
    'satus': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class AdminMovieCommentResource(Resource):
    @marshal_with(source_field)
    def get(self):
        comment_obj = Comment.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': comment_obj
        }
        return data


class AdminMovieCommentDetailResource(Resource):
    def get(self, comment_id):
        comment_obj = Comment.query.get(comment_id)
        db.session.delete(comment_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除评论成功'
        }
        return data
