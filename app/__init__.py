from flask_restx import Api
from flask import Blueprint

from .main.controller.users import api as Users

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(Users, path="/users")