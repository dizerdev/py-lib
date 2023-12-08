from flask import Flask

app = Flask(__name__)

cores_frutas = {
    "morango": "vermelho",
    "uva": "roxo",
    "banana": "amarelo",
    "abacaxi": "amarelo",
    "limão": "verde"
}


# na url, o penultimo parametro quando uma chave, o ultimo parametro pode
# receber qualquer nome acessar o valor da chave
@app.route("/frutas/<nome_fruta>/cor")
def frutas(nome_fruta):
    # verifica se existe a chave que tem mesmo valor do parametro
    if nome_fruta in cores_frutas:
        # se existir, retorna o valor do parametro como chave do dicionario
        return cores_frutas[nome_fruta]
    return "Não sei"


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
