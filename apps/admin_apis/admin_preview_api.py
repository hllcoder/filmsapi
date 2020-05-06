import os
from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask import request
from .commons import change_filename
from apps.settings import BASE_PATH, UPLOAD_FOLDER
from apps.models.models import Preview
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, help='title error')

singer_field = {
    'id': fields.Integer,
    'title': fields.String,
    'logo': fields.String
}

resource_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(singer_field))
}


class AdminPreviewResource(Resource):
    @marshal_with(resource_field)
    def get(self):
        preview_obj = Preview.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': preview_obj
        }
        return data

    def post(self):
        args = parser.parse_args()
        title = args.get('title')
        preview_obj = Preview(title=title)
        logo = request.files['logo']
        file_name = logo.filename
        new_file_name = change_filename(file_name)
        real_path = os.path.join(os.path.join(BASE_PATH, UPLOAD_FOLDER), new_file_name)
        logo.save(real_path)
        preview_obj.logo = UPLOAD_FOLDER + '/' + new_file_name
        db.session.add(preview_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '创建预告成功'
        }
        return data


class AdminPreviewDetailResource(Resource):
    def get(self, preview_id):
        preview_obj = Preview.query.get(preview_id)
        data = {
            'status': 200,
            'msg': 'success',
            'data': marshal(preview_obj, singer_field)
        }
        return data

    def put(self, preview_id):
        preview_obj = Preview.query.get(preview_id)
        args = parser.parse_args()
        title = args.get('title')
        preview_obj.title = title
        logo = request.files['logo']
        file_name = logo.filename
        new_file_name = change_filename(file_name)
        real_path = os.path.join(os.path.join(BASE_PATH, UPLOAD_FOLDER), new_file_name)
        logo.save(real_path)
        preview_obj.logo = UPLOAD_FOLDER + '/' + new_file_name
        db.session.add(preview_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '更新预告成功'
        }
        return data

    def delete(self, preview_id):
        preview_obj = Preview.query.get(preview_id)
        db.session.delete(preview_obj)
        db.session.commit()
        data = {
            'status': 204,
            'msg': '删除预告成功'
        }
        return data
