from flask_restful import Resource, reqparse, fields, marshal_with,marshal
from flask import request
from .commons import change_filename
from apps.models.models import Movie
import os
from apps.settings import BASE_PATH, UPLOAD_FOLDER
from apps.exts import db

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, help='title error')
parser.add_argument('info', required=True, help='info error')
parser.add_argument('star', type=int, required=True, help='star error')
parser.add_argument('tag_id', type=int, required=True, help='tag_id error')
parser.add_argument('area', required=True, help='area error')
parser.add_argument('length', required=True, help='length error')
parser.add_argument('release_time', required=True, help='release time error', )

nest_field = {
    'name': fields.String
}

resource_field = {
    'id': fields.Integer,
    'title': fields.String,
    'length': fields.String,
    'tag': fields.Nested(nest_field),
    'area': fields.String,
    'star': fields.Integer,
    'playnum': fields.Integer,
    'commentnum': fields.Integer,
    'release_time': fields.String
}

all_field = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(resource_field))
}


class AdminMovieResource(Resource):
    def post(self):
        args = parser.parse_args()
        title = args.get('title')
        info = args.get('info')
        star = args.get('star')
        tag_id = args.get('tag_id')
        area = args.get('area')
        length = args.get('length')
        release_time = args.get('release_time')
        url = request.files['url']
        logo = request.files['logo']
        movie_obj = Movie(
            title=title,
            info=info,
            star=star,
            tag_id=tag_id,
            area=area,
            length=length,
            release_time=release_time
        )
        file_name = url.filename
        new_file_name = change_filename(file_name)
        real_path = os.path.join(os.path.join(BASE_PATH, UPLOAD_FOLDER), new_file_name)
        url.save(real_path)
        movie_obj.url = UPLOAD_FOLDER + '/' + new_file_name
        logo_name = logo.filename
        new_logo_name = change_filename(logo_name)
        real_logo_path = os.path.join(os.path.join(BASE_PATH, UPLOAD_FOLDER), new_logo_name)
        logo.save(real_logo_path)
        movie_obj.logo = UPLOAD_FOLDER + '/' + new_logo_name
        db.session.add(movie_obj)
        db.session.commit()
        data = {
            'status': 201,
            'msg': '添加电影成功'
        }
        return data

    @marshal_with(all_field)
    def get(self):
        movie_obj = Movie.query.all()
        data = {
            'status': 200,
            'msg': 'success',
            'data': movie_obj
        }
        return data


class AdminMovieDetailResource(Resource):
    def get(self,movie_id):
        movie_obj = Movie.query.get(movie_id)
        data = {
            'status':200,
            'msg':'获取电影详情成功',
            'data':marshal(movie_obj,resource_field)
        }
        return data

    def put(self,movie_id):
        movie_obj = Movie.query.get(movie_id)
        args = parser.parse_args()
        title = args.get('title')
        info = args.get('info')
        star = args.get('star')
        tag_id = args.get('tag_id')
        area = args.get('area')
        length = args.get('length')
        release_time = args.get('release_time')
        movie_obj.title = title,
        movie_obj.info = info,
        movie_obj.star = star,
        movie_obj.tag_id = tag_id,
        movie_obj.area = area,
        movie_obj.length = length,
        movie_obj.release_time = release_time
        db.session.add(movie_obj)
        db.session.commit()
        data = {
            'status':201,
            'msg':'更新电影成功'
        }
        return data

    def delete(self,movie_id):
        movie_obj = Movie.query.get(movie_id)
        db.session.delete(movie_obj)
        db.session.commit()
        data = {
            'status':204,
            'msg':'删除电影成功'
        }
        return data

