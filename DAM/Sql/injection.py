from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///autentica.db')


def criar_tabela():
    with engine.connect() as con:
        create_tabela_senhas = text("CREATE TABLE IF NOT EXISTS Users (login TEXT NOT NULL,senha TEXT NOT NULL)")
        rs = con.execute(create_tabela_senhas)


def criar_usuarios():
    with engine.connect() as con:
        add_usuaria = text("INSERT INTO Users (login, senha) VALUES ('Minerva', '123')")
        con.execute(add_usuaria)

        add_usuario = text("INSERT INTO Users (login, senha) VALUES ('José', 'Carabina')")
        con.execute(add_usuario)

        add_admin = text("INSERT INTO Users (login, senha) VALUES ('admin','eLl96BFLVsoPrcOJGa0PhvwFnxt7ThKn')")
        con.execute(add_admin)

        con.commit()


def validar_admin_vulneravel(senha):
    with engine.connect() as con:
        sql_admin = text(f"SELECT * FROM users WHERE login='admin' and senha='{senha}'")
        print(sql_admin)
        rs = con.execute(sql_admin)
        result = rs.fetchone()
        if result is None:
            return 'nao autorizado'
        return 'autorizado'
# ataque
    # validar_admin_vulneravel("nao sei' OR 'a'='a")
    # é uma consulta de condição lógica, e nesse caso OR 'a'='a' vai retornar True.


def validar_admin_seguro(senha):
    with engine.connect() as con:
        sql_admin = text("SELECT * FROM users WHERE login='admin' and senha= :senha")
        print(sql_admin)
        rs = con.execute(sql_admin, {"senha": senha})
        result = rs.fetchone()
        if result is None:
            return 'nao autorizado'
        return 'autorizado'


def validar_user_seguro(user, senha):
    with engine.connect() as con:
        sql_admin = text("SELECT * FROM users WHERE login= :user and senha= :senha")
        print(sql_admin)
        rs = con.execute(sql_admin, {"senha": senha, "user": user})
        result = rs.fetchone()
        if result is None:
            return 'nao autorizado'
        return 'autorizado'

# sql injection
    # sql injection é uma vulnerabilidade de segurança que ocorre quando
    # usamos input do usuário para montar a string SQL a ser executada

# prepared statement
    # prepared statement é a proteção contra sql injection
    # criamos strings sql que informam à nossa biblioteca de acesso
    # ao banco de dados qual parte da string é codificada por nós
    # e qual parte é input do usuário
    # no nosso caso, a sintaxe para prepared statement é como no exemplo:
    # sql_admin = text ("SELECT * FROM users WHERE login='admin' and senha= :senha")
    # rs = con.execute(sql_admin , senha=senha)
