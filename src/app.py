from flask import Flask
# Añade el método jsonify a tu importación de Flask
from flask import Flask , jsonify, request


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'



@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    #recordar que hay que importr request from Flask
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        # Eliminamos el elemento por índice
        deleted = todos.pop(position)
        return jsonify(todos)
    
    except IndexError:
        return jsonify({"error": "No existe esa posición"}), 404






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)