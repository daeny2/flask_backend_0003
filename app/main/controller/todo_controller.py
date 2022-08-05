from flask import Flask, request
from flask_restx import Resource

from ..util.dto import TodoDto
#from model import todo  # call model file
from flask_cors import CORS  # to avoid cors error in different frontend like react js or any other
from ..service.todo_service import insert, update, delete, find, find_by_id
from typing import Dict, Tuple

app = Flask(__name__)
CORS(app)

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

@app.route('/', methods=['GET'])
class TaskList(Resource):
    @api.doc('list of todo')
    def get():
        return find({}), 200


    @api.expect(_todo, validate=True)
    @api.response(201, 'Todo successfully created.')
    @api.doc('create a new todo')
    def post(self) -> Tuple[Dict[str, str], int]:
        title = request.form['title']
        body = request.form['body']
        response = insert({'title': title, 'body': body})
        return response, 201




@app.route('/<string:todo_id>/', methods=['GET'])
@api.param('todo_id', 'The Todo identifier')
@api.response(404, 'Todo not found.')
class Task(Resource):
    @api.doc('get a todo')
    def get(self, todo_id):
        #return find_by_id(todo_id), 200
        todo = find_by_id(todo_id)
        if not todo:
            api.abort(404)
        else:
            return todo


@app.route('/<string:todo_id>/', methods=['PUT'])
def update(todo_id):
    title = request.form['title']
    body = request.form['body']
    response = update(todo_id, {'title': title, 'body': body})
    return response, 201


@app.route('/<string:todo_id>/', methods=['DELETE'])
def delete(todo_id):
    delete(todo_id)
    return "Record Deleted"
