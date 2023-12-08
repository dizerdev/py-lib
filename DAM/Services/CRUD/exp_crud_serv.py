from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
app = Flask(__name__)


pessoas = dict()


# função para validar os tipos e quantidade de dados recebidos
def pessoa_ok(dic):
    # retorna um booleano, verificando com 'and' cada uma das condições
    # se alguma retornar false, ela inteira retorna false...
    return type(dic) is dict \
        and len(dic) == 3 \
        and "nome" in dic \
        and "sexo" in dic \
        and "cabelo" in dic \
        and type(dic["nome"]) is str \
        and dic["sexo"] in ["M", "F"] \
        and type(dic["cabelo"]) is str


@app.route("/pessoa", methods=["POST"])
def cadastrar():
    # nomeando n com quantidade de indices no json
    n = len(pessoas)
    # utilizando flask.request no corpo recebido do cliente
    # e atribui na varivavel pessoa com formato json
    pessoa = request.json
    # testando se não for true para pessoa_ok(dic)
    if not pessoa_ok(pessoa):
        # se não atender, manda BadRequest
        raise BadRequest
    # se atender, é indicada primeiro quantidade de indices existentes
    # é atribuido dic pessoa a essa variavel
    pessoas[n] = pessoa
    # e antes de retornar algo, n (numeros existentes) é adicionado mais 1
    n += 1
    # entao o dic pessoas, que indica como indice a variavel n, é retornado
    return pessoas


@app.route("/pessoa/<int:id_pessoa>", methods=["PUT"])
def atualizar(id_pessoa):
    # utilizando flask.request no corpo recebido do cliente
    # e atribui na varivavel pessoa com formato json
    pessoa = request.json
    # verifica se o corpo recebido é diferente de pessoa_ok()
    if not pessoa_ok(pessoa):
        raise BadRequest
    # se for OK, verifica se o inteiro não existe no dic servidor
    if id_pessoa not in pessoas:
        raise NotFound
    # se existir, é indicado primeiro o valor do indice
    # esse indice recebe o corpo enviado e atribuido à pessoa
    pessoas[id_pessoa] = pessoa
    # e então retorna dic pessoas atualizada para o servidor
    return pessoas


@app.route("/pessoa/<int:id_pessoa>", methods=["GET"])
def selecionar(id_pessoa):
    if id_pessoa not in pessoas:
        raise NotFound
    return jsonify(pessoas[id_pessoa])


@app.route("/pessoa/<int:id_pessoa>", methods=["DELETE"])
def deletar(id_pessoa):
    if id_pessoa in pessoas:
        del pessoas[id_pessoa]
    return pessoas


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
