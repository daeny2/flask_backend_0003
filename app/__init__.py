from flask_restx import Api
from flask import Blueprint

#from .main.controller.users import api as Users
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.todo_controller import api as todo_ns


blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='FLASK RESTX API SAMPLE WITH JWT',
          version='1.0',
          description='a sample for flask restx web service',
          authorizations=authorizations,
          security='apikey'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(todo_ns, path='/todo')
