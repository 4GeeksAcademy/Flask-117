# Añade el método jsonify a tu importación de Flask y el request
from flask import Flask , jsonify, request


app = Flask(__name__)# instanciar flask

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
        ]

@app.route('/', methods=['GET'])
def hello_world():
    return'''
    <h1 style="text-align: center; margin-top: 2;">Hello World!</h1>
    '''



@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    #recordar que hay que importr request from Flask
    task_emviada = request.get_json()
    todos.append(task_emviada)
    print("Incoming request with the following body",task_emviada)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        # Eliminamos el elemento por índice
        deleted = todos.pop(position)
        return jsonify(f"el usuario eliminado exitosamente es :{deleted}"),201
    
    except IndexError:
        return jsonify({"error": "No existe esa posición"}), 404






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)