from flask import Flask, make_response, jsonify, redirect
app = Flask(__name__)


@app.route("/exemplo5")
def exemplo5():
    # atribuindo um json à variavel corpo
    corpo = jsonify(["banana", "uva", "laranja"])
    # make
    manipular = make_response(corpo)
    # atribuindo ao atribuito headers um novo par chave:valor
    manipular.headers["X-tipo-dado"] = "frutas"
    manipular.status_code = 275
    return manipular


@app.route("/exemplo6")
def exemplo6():
    # Se code fosse omitido, o 302 seria utilizado por padrão.
    return redirect("/exemplo5", code=305)


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
