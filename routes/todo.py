from flask import jsonify, Blueprint, request
from models.todos import todos

todos_routes = Blueprint('todos', __name__)


@todos_routes.get('/todos')
def get_todos():
    return jsonify({"results": todos})


@todos_routes.get("/todos/<string:id>")
def get_todos_by_id(id):
    result = [todo for todo in todos if todo["id"] == id]
    if (len(result) > 0):
        return jsonify({"result": result[0]}), 200
    return jsonify({"message": "Item was not found in the database"}), 404


@todos_routes.delete("/todos/<string:id>")
def delete_todo_by_id(id):
    item = [todo for todo in todos if todo["id"] == id]

    if (len(item) <= 0):
        return jsonify({"message": "todo was not found"})
    return jsonify({"message": "todo was succesfuly removed"}), 200


@todos_routes.put("/todos/<string:id>")
def update_todo_by_id(id):
    index = [index for (index, todo) in enumerate(todos)
             if todo["id"] == id]
    if (len(index) <= 0):
        return jsonify({"message": "Todo was not found"})

    for key in request.json.keys():
        todos[index[0]][key] = request.json[key]

    return jsonify({"messsage": "updated todo", "todo": todos[index[0]]}), 200
