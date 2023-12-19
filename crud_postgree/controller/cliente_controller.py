import model.cliente_model as cliente_model
from flask import jsonify


# ########## SEED DATABASE ###########
def create_table_register():
    cliente_model.register_table()
    return 'response'


def create_table_client():
    cliente_model.client_table()
    return 'response'


def create_table_product():
    cliente_model.product_table()
    return 'Tabela criada com sucesso'


# ########## CREATE ##########
def insert_new_register(new_register):
    name = new_register.get('name')
    email = new_register.get('email')
    password = new_register.get('password')
    cliente_model.insert_register(name, email, password)
    return 'Inserido com sucesso'


def insert_new_product(new_product):
    name = new_product.get('name')
    category = new_product.get('category')
    quantity = new_product.get('quantity')
    cost = new_product.get('cost')
    sale = new_product.get('sale')
    description = new_product.get('description')
    cliente_model.insert_product(name,
                                 category,
                                 quantity,
                                 cost,
                                 sale,
                                 description)
    return 'Inserido com sucesso'


# ########## READ ##########
def find_by_cod(cod_register):
    resposta = cliente_model.find_register(cod_register)
    if resposta is None:
        return "Registro não foi encontrado"
    return jsonify(resposta)


def find_product_name(text):
    resposta = cliente_model.find_product(text)
    if resposta == []:
        return "Produto não foi encontrado"
    return jsonify(resposta)


# ########## UPDATE ##########
def update_by_cod(updated_product):
    cod_product = updated_product.get('cod_product')
    name = updated_product.get('name')
    category = updated_product.get('category')
    quantity = updated_product.get('quantity')
    cost = updated_product.get('cost')
    sale = updated_product.get('sale')
    description = updated_product.get('description')
    cliente_model.update_product(cod_product,
                                 name,
                                 category,
                                 quantity,
                                 cost,
                                 sale,
                                 description)
    return "Alterado com sucesso"


# ########## DELETE ##########
def delete_by_cod(deleted_product):
    cod_product = deleted_product.get('cod_product')
    cliente_model.delete_product(cod_product)
    return "Deletado com sucesso"
