from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
