from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok

import controller.aluno_controller as aluno_controller

app = Flask(__name__) 
ngrok.set_auth_token("275JW9XPjdA0oXh9lcsl7NiTchd_6S3nK3dU59S8EvQ5MFHQJ")
run_with_ngrok(app)  # inicia ngrok quando app está executando

@app.route('/alunos')
def getAlunos():
    return aluno_controller.listar() 

@app.route("/alunos/<int:id_consulta>", methods=["GET"])
def getAlunoId(id_consulta):
    return aluno_controller.localizaPorId(id_consulta)

@app.route("/alunos/maior_media", methods=["GET"])
def getAlunoMaiorMedia():
    return aluno_controller.localizarPorMaiorMedia()
	
@app.route("/alunos", methods=["POST"])	
def inserir():
	aluno = request.get_json(force=True)
	return aluno_controller.inserirAluno(aluno)

@app.route("/alunos/<int:id_deletar>", methods=["DELETE"])
def excluir(id_deletar):
	return aluno_controller.excluirPorId(id_deletar)

@app.route("/alunos/<int:id_alterar>", methods=["PUT"])	
def alterar(id_alterar):
	aluno = request.get_json(force=True)
	return aluno_controller.alterarAluno(id_alterar, aluno)
	
@app.route('/')
def start():
    return "Construindo nossa aplicação com MVC"

if __name__ == '__main__':
    app.run() 