import os
import unittest
import click

from flask_migrate import Migrate
#from flask_script import Manager

from flask.cli import FlaskGroup

from app.main import create_app, db
from app.main.model import users
from app import blueprint


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()


cli = FlaskGroup(app)

#manager = Manager(app)

migrate = Migrate()
migrate.init_app(app, db)
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)

#@manager.command
#def run():
#	app.run()

 

@cli.command('test')
@click.argument('test_case', default='test*.py')
def test(test_case='test*.py'):
#@manager.command
#def test():
	# Runs the unit tests.
	tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

if __name__ == '__main__':
	#manager.run()
    cli()