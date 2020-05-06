from flask_restful import Resource, marshal_with, fields
from apps.models.models import Preview

singal_field = {
    'id': fields.Integer,
    'logo': fields.String,
    'title': fields.String
}

source_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singal_field))
}


class MovieAnimationResource(Resource):
    @marshal_with(source_field)
    def get(self):
        preview_obj = Preview.query.order_by(Preview.add_time.desc()).all()
        data = {
            'status': 200,
            'msg': '获取电影预告成功',
            'data': preview_obj
        }
        return data
