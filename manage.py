from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Pitch
app = create_app('development')


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
'''
adds the databse instance and models to the shell session
'''
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch =Pitch )
    
if __name__ == '__main__':
    manager.run()