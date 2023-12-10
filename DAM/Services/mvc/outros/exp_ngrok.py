from flask import Flask
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok
# from ngrok import ngrok

app = Flask(__name__)

ngrok.set_auth_token("")
run_with_ngrok(app)


@app.route('/')
def start():
    return 'Seja bem-vindo na aula de Desevolvimento de APIs e Microsserviços.'


if __name__ == '__main__':
    app.run()

# necessario apontar o tunel em outro terminal com comando:
# ngrok http 5000
