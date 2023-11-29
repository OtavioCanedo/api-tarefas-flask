from flask import Flask
from requests import post
from bd import Tasks

app = Flask(__name__)

def createTask():
  node_url = "http://localhost:3000/createTasks"

  task_data = {
      "name": "Documentar código",
      "description": "Criar documentação clara e detalhada para as 2 APIs",
      "priority": "medium",
      "status": "todo"
    }
  
  response = post(node_url, task_data)
  print('Resposta da requisição da API Node:', response.json())

  if response.status_code == 200:
    return {"message": "Tarefa criada com sucesso no aplicativo Node.js"}
  else:
    return {"error": f"Erro ao criar tarefa. Código de status: {response.status_code}"}
  
createTask()

@app.route("/getTasks", methods=["GET"])
def getTasks():
  print(Tasks)
  return Tasks

if __name__ == "__main__":
    app.run()