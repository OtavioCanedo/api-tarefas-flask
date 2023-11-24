from flask import Flask
from requests import post
from bd import Tasks

app = Flask(__name__)

def createTask():
  node_url = "http://localhost:3000/createTasks"

  tasks_data = [
    {
      "name": "Testar funcionalidades",
      "description": "Realizar testes de unidade e integração nas funcionalidades do sistema",
      "priority": "medium",
      "status": "todo"
    },
    {
      "name": "Otimizar desempenho",
      "description": "Identificar e implementar otimizações para melhorar o desempenho do sistema",
      "priority": "high",
      "status": "todo"
    },
    {
      "name": "Documentar código",
      "description": "Criar documentação clara e detalhada para o código-fonte do projeto",
      "priority": "low",
      "status": "todo"
    }
  ]
  
  response = post(node_url, json=tasks_data)
  print('Resposta da requisição da API Node:', response.json())

  if response.status_code == 200:
    return {"message": "Tarefa criada com sucesso no aplicativo Node.js"}
  else:
    return {"error": f"Erro ao criar tarefa. Código de status: {response.status_code}"}
  
createTask()

@app.route("/getTasks", methods=["GET"])
def getTasks(): 
  return Tasks

if __name__ == "__main__":
    app.run()