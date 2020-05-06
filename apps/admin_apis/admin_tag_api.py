from flask_restful import Resource, reqparse, abort, fields, marshal_with
from apps.models.models import Tag
from apps.exts import db
from .commons import decorate

parser = reqparse.RequestParser()
parser.add_argument('tag_name', required=True, help='tag name error')

nest_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'add_time': fields.DateTime()
}

singal_fields = {
    'data': fields.Nested(nest_fields),
    'status': fields.Integer,
    'msg': fields.String,
}

resource_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(nest_fields))
}


class AdminTagResource(Resource):
    @decorate
    def post(self):
        args = parser.parse_args()
        tag_name = args.get('tag_name')
        tag_count = Tag.query.filter_by(name=tag_name).count()
        if tag_count:
            abort(404, message='标签名已存在')
        tag_obj = Tag(name=tag_name)
        db.session.add(tag_obj)
        db.session.commit()

        data = {
            'status': 201,
            'msg': '添加标签成功'
        }

        return data

    @decorate
    @marshal_with(resource_field)
    def get(self):
        tag_content = Tag.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': tag_content
        }
        return data


class AdminTagDetailResource(Resource):
    @marshal_with(singal_fields)
    def get(self, tag_id):
        tag_obj = Tag.query.get(tag_id)
        data = {
            'status': 200,
            'msg': 'success',
            'data': tag_obj
        }
        return data

    def put(self, tag_id):
        args = parser.parse_args()
        name = args.get('tag_name')
        tag_obj = Tag.query.get(tag_id)
        tag_obj.name = name
        db.session.add(tag_obj)
        db.session.commit()
        data = {
            'status':201,
            'msg':'更新标签成功'
        }
        return data

    def delete(self, tag_id):
        tag_obj = Tag.query.get(tag_id)
        db.session.delete(tag_obj)
        db.session.commit()
        data = {
            'status':204,
            'msg':'删除标签成功'
        }
        return data
