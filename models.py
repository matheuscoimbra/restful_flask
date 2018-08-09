# coding:utf-8
from flask_mongoengine import MongoEngine

db = MongoEngine()
"""

Modelagem da classe Consumidor

"""
class Reclamacao(db.Document):


    titulo = db.StringField(max_length=50, required=True)
    descricao = db.StringField(required=True)
    local = db.StringField(max_length=60, required=True)
    companhia = db.StringField(required=True)



