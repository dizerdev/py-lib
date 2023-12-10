from flask import Flask
from flask import jsonify
from flask import request

import controller.aluno_controller as aluno_controller

app = Flask(__name__) 

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
    app.run(host = 'localhost', port = 5002, debug = True) 