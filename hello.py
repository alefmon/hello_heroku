import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! <br>Esta é a parte 1 do TP de Engenharia de Software. <br> Alunos: Alef Monteiro e Gabriel Cardoso.'

