from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def boasVindas():
    nome = request.get_json(force=True)
    return 'Seja bem-vindo, {}, na aula de Desevolvimento de APIs e Micro-serviços.\n'.format(nome['nome'])


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)

# forma de testar a rota direto no terminal
# curl -H \Content-Type:application/json\ -X POST --data "{\"nome\":\"Diego\"}" http://localhost:5002
