from flask_restx import Api
from flask import Blueprint

#from .main.controller.users import api as Users
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restx web service',
          authorizations=authorizations,
          security='apikey'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)