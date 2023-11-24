from flask import Flask
from bd import Tasks

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def getTasks(): 
  return Tasks

app.run()