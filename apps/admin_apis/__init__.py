from flask_restful import Api
from .admin_login_api import AdminUserLoginResource
from .admin_user_pwd_api import AdminUserPwdResource
from .admin_tag_api import AdminTagResource,AdminTagDetailResource
from .admin_movie_api import AdminMovieResource,AdminMovieDetailResource
from .admin_preview_api import AdminPreviewResource,AdminPreviewDetailResource
from .admin_member_api import AdminMemberResource,AdminMemberDetailResource
from .admin_movie_comment_api import AdminMovieCommentResource,AdminMovieCommentDetailResource
from .admin_moviecol_api import AdminMovieColResource,AdminMovieColDetailResource
from .admin_log_api import AdminOpLogResource,AdminLogResource,UserLogResource
from .admin_auth_apis import AdminAuthResource,AdminAuthDetailResource
from .admin_role_api import AdminRoleResource,AdminRoleDetailResource
from .admin_index_api import AdminIndexResource
from .admin_user_api import AdminUserResource


api = Api(prefix='/admin')


def init_admin_api(app):
    api.init_app(app)

api.add_resource(AdminIndexResource, '/index/')
api.add_resource(AdminUserLoginResource, '/login/')
api.add_resource(AdminUserPwdResource,'/pwd/')
api.add_resource(AdminTagResource,'/tag/')
api.add_resource(AdminTagDetailResource,'/tag/<int:tag_id>/')
api.add_resource(AdminMovieResource,'/movie/')
api.add_resource(AdminMovieDetailResource,'/movie/<int:movie_id>/')
api.add_resource(AdminPreviewResource,'/preview/')
api.add_resource(AdminPreviewDetailResource,'/preview/<int:preview_id>/')
api.add_resource(AdminMemberResource,'/user/')
api.add_resource(AdminMemberDetailResource,'/user/<int:user_id>/')
api.add_resource(AdminMovieCommentResource,'/comments/')
api.add_resource(AdminMovieCommentDetailResource,'/comments/<int:comment_id>/')
api.add_resource(AdminMovieColResource,'/moviecols/')
api.add_resource(AdminMovieColDetailResource,'/moviecols/<int:moviecol_id>/')
api.add_resource(AdminOpLogResource,'/oplogs/')
api.add_resource(AdminLogResource,'/adminlogs/')
api.add_resource(UserLogResource,'/userlogs/')
api.add_resource(AdminAuthResource,'/auths/')
api.add_resource(AdminAuthDetailResource,'/auths/<int:auth_id>/')
api.add_resource(AdminRoleResource,'/roles/')
api.add_resource(AdminRoleDetailResource,'/roles/<int:role_id>/')
api.add_resource(AdminUserResource,'/adminusers/')