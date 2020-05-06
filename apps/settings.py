import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_FOLDER = 'static/upload'


def mysql_url(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE):
    return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                        DATABASE)


class Config:
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'xxxx'  # mysql数据库的账号
    PASSWORD = 'xxxxx'  # mysql数据库的密码
    HOST = 'xxxxxxx'  # mysql数据库的主机  如 '192.168.101.13'
    PORT = 'xxxx'  # mysql数据库的端口  '3306'
    DATABASE = 'xxxxx'  # 使用mysql数据库的具体数据库名称
    SECRET_KEY = '121D3ASASD3*&%^'
    CACHE_TYPE = 'redis'  # 设置缓存为redis
    CACHE_REDIS_HOST = 'xxxxxxx'  # 缓存redis的主机   如 '192.168.101.13'
    CACHE_REDIS_PORT = 'xxxx'  # 缓存redis的端口 '6379'

    SQLALCHEMY_DATABASE_URI = mysql_url(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'xxxxx'
    PASSWORD = 'xxxxxx'
    HOST = 'xxxxx'
    PORT = 'xxxxx'
    DATABASE = 'xxxxxx'

    SQLALCHEMY_DATABASE_URI = mysql_url(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'default': DevelopConfig
}
