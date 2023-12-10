from flask import Flask, jsonify, Blueprint


professores_app = Blueprint('professores_app', __name__, template_folder='templates')


database = {'PROFESSOR': [{"id": 1, "nome": "Professor1"},
                          {"id": 2, "nome": "Professor2"},
                          {"id": 3, "nome": "Professor3"}]}


# rota /professores padrão GET: retorna todos os professores
@professores_app.route('/professores')
def getProfessores():
    return jsonify(database['PROFESSOR'])
