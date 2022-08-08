from flask import request
from flask_restx import Resource

#from model import todo  # call model file
#from app.main.util.decorator import admin_token_required
from ..util.dto import TodoDto
from ..service.todo_service import Todo #create, update, delete, find, find_by_id
from typing import Dict, Tuple

#app = Flask(__name__)
#CORS(app)

api = TodoDto.api
_todo = TodoDto.todo
#todo = todo.Todo()


"""
@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        #List all registered users
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        #Creates a new User
        data = request.json
        return save_new_user(data=data)
"""

# todo routes

@api.route('/')
class TaskList(Resource):
    @api.doc('list of todo')
    def get(self):
        """List all Todo"""
        return Todo.find({}), 200

    @api.expect(_todo, validate=True)
    @api.response(201, 'Todo successfully created.')
    @api.doc('create a new todo')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Create a new Todos"""
        title = request.form['title']
        body = request.form['body']
        response = Todo.create({'title': title, 'body': body})
        return response, 201


@api.route('/<string:todo_id>')
@api.param('todo_id', 'The Todo identifier')
@api.response(404, 'Todo not found.')
class Task(Resource):
    @api.doc('get a todo')
    def get(self, todo_id):
        """Get a Todos"""
        #return find_by_id(todo_id), 200
        todo = Todo.find_by_id(todo_id)
        if not todo:
            api.abort(404)
        else:
            return todo

    @api.doc('update a todo')
    def put(self, todo_id):
        """Update a Todos"""
        title = request.form['title']
        body = request.form['body']
        response = Todo.update(todo_id, {'title': title, 'body': body})
        return response, 201


    @api.doc('deletee a todo')
    def delete(self, todo_id):
        """Delete a Todos"""
        Todo.delete(todo_id)
        return "Record Deleted"
