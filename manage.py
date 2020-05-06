from flask_script import Manager
from apps import create_app
from apps.exts import db
from flask_migrate import Migrate,MigrateCommand
import os

env = os.environ.get('FLASK_ENV') or 'default'

app = create_app(env)

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
