1.pip install -r requirements.txt

2.在apps里面的settings配置整个项目的初始化配置

3.在目录下包含manage.py的项目目录下运行如下命令
    1. python manage.py db init 初始化数据库
    2. python manage.py db migrate 数据库迁移
    3. python manage.py db upgrade 映射到数据库中
    执行完命令项目目录下会出现 migrations文件夹

4.执行python manage.py runserver开启项目本地服务器

