from flask_restful import Api
from .user_register_api import UserRegisterResource
from .user_login_api import UserLoginResource
from .user_api import UserResource, UserDetailResource
from .user_pwd_api import UserPwdResource
from .user_comments_api import UserCommentResource
from .user_log_api import UserLogDetailResource
from .user_moviecol_api import UserMovieColResource, UserMovieColDetailResource
from .movie_animation_api import MovieAnimationResource
from .movie_search_api import MovieSearchResource
from .movie_play_api import MoviePlayResource
from .home_index_api import HomeIndexResource

api = Api()


def init_home_api(app):
    api.init_app(app)


api.add_resource(HomeIndexResource, '/index/')
api.add_resource(UserRegisterResource, '/register/')
api.add_resource(UserLoginResource, '/login/')
api.add_resource(UserDetailResource, '/user/<int:user_id>/')
api.add_resource(UserResource, '/user/')
api.add_resource(UserPwdResource, '/pwd/')
api.add_resource(UserCommentResource, '/comments/')
api.add_resource(UserLogDetailResource, '/logs/')
api.add_resource(UserMovieColResource, '/usermoviecols/')
api.add_resource(UserMovieColDetailResource, '/usermoviecols/<int:movie_id>/')
api.add_resource(MovieAnimationResource, '/animation/')
api.add_resource(MovieSearchResource, '/search/')
api.add_resource(MoviePlayResource, '/play/<int:movie_id>/')
