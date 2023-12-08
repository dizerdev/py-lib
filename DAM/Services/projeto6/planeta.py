from flask import Flask, render_template
app = Flask(__name__)


@app.route("/visitar/<planeta>")
def visitar_planeta(planeta):
    return "OK"


@app.route("/planetas")
def listar_planetas_visitados_recentemente():
    return render_template("planetas.html")


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
