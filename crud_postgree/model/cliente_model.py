from db.db import conn


# ########## SEED DATABASE ###########
def register_table():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS TB_CADASTRO
                           (COD_CADASTRO SERIAL PRIMARY KEY NOT NULL,
                            NOME_COMPLETO VARCHAR(50) NOT NULL,
                            E_MAIL VARCHAR(50) UNIQUE NOT NULL,
                            SENHA VARCHAR(64) NOT NULL,
                            DATA_CADASTRO TIMESTAMP DEFAULT NOW())""")
            conn.commit()
            cursor.close()
    return {'message': 'Success'}, 201


def client_table():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS TB_CLIENTE
                           (COD_CLIENTE SERIAL PRIMARY KEY NOT NULL,
                           NOME_COMPLETO VARCHAR(50) NOT NULL,
                           E_MAIL VARCHAR(50) UNIQUE NOT NULL,
                           ENDERECO VARCHAR(60) NOT NULL,
                           REFERENCIA VARCHAR(60),
                           BAIRRO VARCHAR(20) NOT NULL,
                           CIDADE VARCHAR(20) NOT NULL,
                           ESTADO VARCHAR(2) NOT NULL,
                           CEP VARCHAR(8) NOT NULL,
                           TELEFONE VARCHAR(11) NOT NULL,
                           DATA_CADASTRO TIMESTAMP DEFAULT NOW())""")
            conn.commit()
            cursor.close()
    return {'message': 'Success'}, 201


def product_table():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS TB_PRODUTO
                           (COD_PRODUTO SERIAL PRIMARY KEY NOT NULL,
                           NOME VARCHAR(60) NOT NULL,
                           COD_CATEGORIA INTEGER NOT NULL,
                           QTD_ESTOQUE NUMERIC(10,2) NOT NULL,
                           PRECO_CUSTO NUMERIC(10,2) NOT NULL,
                           PRECO_VENDA NUMERIC(10,2) NOT NULL,
                           DESCRICAO VARCHAR(200) NOT NULL)""")
            conn.commit()
            cursor.close()
    return {'message': 'Success'}, 201


# ########## CREATE ##########
def insert_register(name, email, password):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""INSERT INTO TB_CADASTRO
                           (nome_completo, e_mail, senha)
                           VALUES (%s, %s, %s)""", (
                               name,
                               email,
                               password))
            conn.commit()
            cursor.close()
    return {'message': 'Success'}, 201


def insert_product(name, category, quantity, cost, sale, description):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""INSERT INTO TB_PRODUTO
                           (nome, cod_categoria,
                           qtd_estoque, preco_custo,
                           preco_venda, descricao)
                           VALUES (%s, %s, %s, %s, %s, %s)""", (
                               name,
                               category,
                               quantity,
                               cost,
                               sale,
                               description))
            conn.commit()
            cursor.close()
    return {'message': 'Success'}, 201


# ########## READ ##########
def find_register(cod_register):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""SELECT * FROM
                           TB_CADASTRO WHERE
                           cod_cadastro = %s""", (cod_register,))
            result = cursor.fetchone()
            cursor.close()
            return result


def find_product(text):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""SELECT * FROM
                           TB_PRODUTO WHERE
                           nome ILIKE %s""", ('%' + text + '%',))
            results = cursor.fetchall()
            cursor.close()
            return results


# ########## UPDATE ##########
def update_product(cod_product,
                   name,
                   category,
                   quantity,
                   cost,
                   sale,
                   description):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""UPDATE TB_PRODUTO
                           SET nome = %s, cod_categoria = %s,
                           qtd_estoque = %s, preco_custo = %s,
                           preco_venda = %s, descricao = %s
                           WHERE cod_produto = %s""",
                           (name,
                            category,
                            quantity,
                            cost,
                            sale,
                            description,
                            cod_product,))
            conn.commit()
            cursor.close()
            return {'message': 'Success'}, 201


# ########## DELETE ##########
def delete_product(cod_product):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""DELETE FROM tb_produto
                           WHERE cod_produto = %s""", (cod_product,))
            conn.commit()
            cursor.close()
            return {'message': 'Success'}, 201
