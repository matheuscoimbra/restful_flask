from flask import jsonify, request, abort
from application import app
from models import Reclamacao
from mongoengine.queryset.visitor import Q
from util import less_common,most_common
import json


# retorna local com mais reclamações
@app.route("/reclamacao/mais/local", methods=["GET"])
def get_complain_most_locale():
    lista = list()
    for rec in Reclamacao.objects:
        lista.append(rec.local)
    l = most_common(lista)
    return jsonify({
        'local': l,
    })

# retorna local com menos reclamações
@app.route("/reclamacao/menos/local", methods=["GET"])
def get_complain_less_locale():
    lista = list()
    for rec in Reclamacao.objects:
        lista.append(rec.local)
    l = less_common(lista)
    return jsonify({
        'local': l,
    })

# retorna companhia com mais reclamações
@app.route("/reclamacao/mais/companhia", methods=["GET"])
def get_complain_most_company():
    lista = list()
    for rec in Reclamacao.objects:
        lista.append(rec.companhia)
    l = most_common(lista)
    return jsonify({
        'empresa': l,
    })

# retorna companhia com menos reclamações
@app.route("/reclamacao/menos/companhia", methods=["GET"])
def get_complain_less_company():
    lista = list()
    for rec in Reclamacao.objects:
        lista.append(rec.companhia)
    #print(lista)
    l = less_common(lista)
    return jsonify({
        'empresa': l,
    })

# cria uma reclamação
@app.route("/reclamacao", methods=["POST"])
def add_complain():
    reclamacao = Reclamacao()
    reclamacao.titulo = str(request.json['titulo'])
    reclamacao.descricao = str(request.json['descricao'])
    reclamacao.local = str(request.json['local'])
    reclamacao.companhia = str(request.json['companhia'])
    reclamacao.save()

    return jsonify(reclamacao)

# retorna quantidade de reclamações de uma empresa de determinada localidade
@app.route("/reclamacao/<companhia>/<local>", methods=["GET"])
def get_complain_company_region(companhia,local):
    reclamacao = len(Reclamacao.objects((Q(companhia=str(companhia)) & Q(local=str(local)))))

    return jsonify({
        'quantidade_consumidores': reclamacao,
    })

# retorna quantidade de reclamações de uma companhia
@app.route("/reclamacao/quantidade/<companhia>", methods=["GET"])
def get_company_quant_comp(companhia):
    qntd_reclamacoes = len(Reclamacao.objects(companhia=str(companhia)))

    return jsonify({
        'quantidade_reclamacoes': qntd_reclamacoes,
    })


# retorna todas as reclamações
@app.route("/reclamacao", methods=["GET"])
def get_complain():
    reclamacao = Reclamacao.objects().all()

    result = reclamacao.to_json()
    python_dictionary = json.loads(result)
    return jsonify(python_dictionary)


# retorna reclamação especificada por id
@app.route("/reclamacao/<id>", methods=["GET"])
def complain_detail(id):
    reclamacao = Reclamacao.objects(id=id).first()
    if not reclamacao:
        abort(404, message="Reclamacao {} não existe!".format(id))
    result = reclamacao.to_json()
    python_dictionary = json.loads(result)
    return jsonify(python_dictionary)


# atualiza os dados de uma reclamação
@app.route("/reclamacao/<id>", methods=["PUT"])
def complain_update(id):
    reclamacao = Reclamacao.objects(id=id).first()
    if not reclamacao:
        abort(404, message="Reclamacao {} não existe!".format(id))
    reclamacao.titulo = request.json['titulo']
    reclamacao.descricao = request.json['descricao']
    reclamacao.local = request.json['local']
    reclamacao.companhia = request.json['companhia']
    reclamacao.save()
    result = reclamacao.to_json()
    python_dictionary = json.loads(result)
    return jsonify(python_dictionary)



# deleta uma reclamação
@app.route("/reclamacao/<id>", methods=["DELETE"])
def complain_delete(id):
    print(type(id))
    reclamacao = Reclamacao.objects(id=id).first()
    if not reclamacao:
        abort(404, message="Reclamacao {} não existe!".format(id))
    reclamacao.delete()
    result = reclamacao.to_json()
    python_dictionary = json.loads(result)
    return jsonify(python_dictionary)
