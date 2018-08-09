# -*- coding: utf-8 -*-
from flask import Flask
from models import db

"""
=============================================
RESTFUL APPLICATION FLASK
@Autor: Matheus Coimbra Moraes

=============================================

execution: python application.py

==============================================
teste: 

curl -X GET \
  http://127.0.0.1:5000/reclamacao \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 2dbfa3d8-ae5a-572b-dc13-9507657ab40e' \
  -d '{"titulo":"produto nao chedgou3",
"descricao":"notebook ainda não edffd c2hegou3",
"local":"amapa",
"companhia":"teste"}'

------ OR -------

GET /reclamacao HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json

------ OR -------

Use Postman application.

GET http://127.0.0.1:5000/reclamacao

==============================================

1: To run the application:
    - install Python3
    - install a virtual env (pip install virtualenv)
    - acess project folder and create the virtual environment with -> virtualenv venv
    - activate the virtual environment with -> venv/scripts/activate (linux)   venv\\bin\\activate
    - pip install -r requirements.txt
    - python application.py

2: Database deployed already at cloud.

3: Valeu!!!

"""

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

from views import *
#inicia a aplicação
if __name__ == '__main__':
    app.run()
