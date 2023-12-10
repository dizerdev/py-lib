# aula12_exemplo1.py na versão com flask_ngrok
from flask import Flask, request
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok


app = Flask(__name__)
ngrok.set_auth_token("")
run_with_ngrok(app)  # inicia ngrok quando app está executando


@app.route('/', methods=['POST'])
def boasVindas():
    nome = request.get_json(force=True)
    return 'Seja bem-vindo, {}, na aula de Desevolvimento de APIs e Microsserviços.\n'.format(nome['nome'])


if __name__ == '__main__':
    app.run()

# necessario apontar o tunel em outro terminal com comando:
# ngrok http 5000
