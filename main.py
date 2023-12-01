from flask import Flask, jsonify, request
from requests import post, exceptions
from bd import Tasks

app = Flask(__name__)

@app.route("/apiNode", methods=["POST"])
def createTask():
    node_url = "http://localhost:3000/createTasks"

    try:
        task_data = request.json

        if not task_data or not isinstance(task_data, dict):
            return {"error": "Dados inválidos no corpo da solicitação"}

        response = post(node_url, json=task_data)
        response.raise_for_status()

        print('Resposta da requisição da API Node:', response.json())
        
        return {"message": "Tarefa criada com sucesso!"}
    except exceptions.RequestException as e:
        return {"error": f"Erro na requisição para a API Node.js: {str(e)}"}

@app.route("/getTasks", methods=["GET"])
def getTasks():
  print(Tasks)
  return Tasks

if __name__ == "__main__":
    app.run()