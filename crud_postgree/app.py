from flask import Flask
import controller.cliente_controller as controller
from flask import request


app = Flask(__name__)


@app.route('/')
def home():
    return "Criando um Crud com PostgreSQL"


# ########## SEED DATABASE ###########
@app.route('/seed-product')
def seed_product():
    controller.create_table_product()
    return "Tabela Criada"


@app.route('/seed-register')
def seed_register():
    controller.create_table_register()
    return "Tabela Criada"


@app.route('/seed-client')
def seed_client():
    controller.create_table_client()
    return "Tabela Criada"


# ########## CREATE ##########
@app.route('/new-resgister', methods=['POST'])
def new_register():
    register = request.json
    controller.insert_new_register(register)
    return 'Inserido com sucesso'


@app.route('/new-product', methods=['POST'])
def new_product():
    product = request.json
    controller.insert_new_product(product)
    return 'Inserido com sucesso'


# ########## READ ##########
@app.route('/register/<int:cod_register>')
def find_register(cod_register):
    return controller.find_by_cod(cod_register)


@app.route('/product/<string:text>')
def find_product(text):
    return controller.find_product_name(text)


# ########## UPDATE ##########
@app.route('/update-product', methods=['PUT'])
def update_product():
    product = request.json
    controller.update_by_cod(product)
    return "Alterado com sucesso"


# ########## DELETE ##########
@app.route('/delete-product', methods=['DELETE'])
def delete_product():
    product = request.json
    controller.delete_by_cod(product)
    return "Deletado com sucesso"


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
