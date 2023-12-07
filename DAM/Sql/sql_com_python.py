from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')

# mas se quisesse uma solução mais robusta, poderia usar mudando o código muito pouco engine = create_engine('postgresql://usuario:senha@localhost:5432/dizerdev')


# criar a tabela
def criar_tabelas():
    with engine.connect() as con:

        create_tabela_aluno = text("CREATE TABLE IF NOT EXISTS Aluno (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, email TEXT NOT NULL UNIQUE)")
        rs = con.execute(create_tabela_aluno)

        create_tabela_livro = text("CREATE TABLE IF NOT EXISTS Livro (id_livro INTEGER PRIMARY KEY, id_aluno INTEGER, descricao TEXT NOT NULL, FOREIGN KEY(id_aluno) REFERENCES Aluno(id))")
        rs = con.execute(create_tabela_livro)


def criar_alunos():
    with engine.connect() as con:
        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (4,'Diego', 'teste@exemplo.com')")
        rs = con.execute(add_aluno)

        con.commit()


def criar_livros():
    with engine.connect() as con:
        add_livro = text("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1, 1, 'Python completo e total')")
        rs = con.execute(add_livro)

        add_livro = text("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (2, 2, 'Memorias póstumas de brás cubas')")
        rs = con.execute(add_livro)

        add_livro = text("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3, 3, 'Gravidade')")
        rs = con.execute(add_livro)

        con.commit()
# criar_tabelas()
# criar_alunos()


class AlunoNaoExisteException(Exception):
    pass
# estamos definindo uma classe AlunoNaoExisteException, que
# herda todas as funcionalidades, todos os métodos e atributos,
# de Exception
# no lugar do pass, escreveríamos as mudanças,
# as coisas que AlunoNaoExisteException faz diferente de Exception
# mas não fizemos mudança nenhuma (por isso pass)


# 1) Crie uma função consulta_aluno que recebe a id de um aluno e devolve um dicionário com os dados desse aluno
def consulta_aluno(id_aluno):
    with engine.connect() as con:
        sql_consulta = text(f"SELECT * FROM aluno WHERE id = {id_aluno}")
        rs = con.execute(sql_consulta)
        colunas = ["id", "nome", "email"]
        result = rs.fetchone()
        d_result = {coluna: valor for coluna, valor in zip(colunas, result)}
        if result is None:
            raise AlunoNaoExisteException
        return d_result


# 1b) Crie uma função todos_alunos que retorna um lista com um dicionario para cada aluno do banco de dados
def todos_alunos():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        colunas = ["id", "nome", "email"]
        resultado = []
        while True:
            result = rs.fetchone()
            if result is None:
                break
            d_result = {coluna: valor for coluna, valor in zip(colunas, result)}
            resultado.append(d_result)
        return resultado


# 1c) Crie uma função todos_livros que retorna um lista com um dicionario para cada livro
def todos_livros():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM Livro")
        rs = con.execute(sql_consulta)
        colunas = ["id_livro", "id_aluno", "descricao"]
        resultado = []
        while True:
            result = rs.fetchone()
            if result is None:
                break
            d_result = {coluna: valor for coluna, valor in zip(colunas, result)}
            resultado.append(d_result)
        return resultado


# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição) e o adiciona no banco de dados
def cria_livro(id_livro, descricao):
    try:
        with engine.connect() as con:
            sql_create = text("INSERT INTO Livro (id_livro, descricao) VALUES (:id_livro, :descricao)")
            con.execute(sql_create, {"id_livro": id_livro, "descricao": descricao})
            con.commit()
    except Exception as e:
        print(f"Erro durante a execução do SQL: {e}")


# 3) Crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno e marca o livro como emprestado pelo aluno"
def empresta_livro(id_aluno, id_livro):
    with engine.connect() as con:
            sql_create = text("UPDATE Livro SET id_aluno=:id_aluno WHERE id_livro = :id_livro;")
            con.execute(sql_create, {"id_aluno": id_aluno, "id_livro": id_livro})
            con.commit()


# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro como disponível
def devolve_livro(id_livro):
    with engine.connect() as con:
            sql_create = text("UPDATE Livro SET id_aluno=NULL WHERE id_livro = :id_livro;")
            con.execute(sql_create, {"id_livro": id_livro})
            con.commit()


# 5) Crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados por ninguém (uma lista de dicionários, um para cada livro)
def livros_parados():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM Livro WHERE id_aluno IS NULL")
        rs = con.execute(sql_consulta)
        colunas = ["id_livro", "id_aluno", "descricao"]
        resultado = []
        while True:
            result = rs.fetchone()
            if result is None:
                break
            d_result = {coluna: valor for coluna, valor in zip(colunas, result)}
            resultado.append(d_result)
        return resultado


# 6) Crie uma função livros_do_aluno, recebe o nome do aluno e devolve a lista de todos os livros que estão com o aluno no momento
def livros_do_aluno(nome):
    with engine.connect() as con:
        sql_consulta = text("SELECT id_livro, id_aluno, descricao FROM Livro JOIN Aluno ON Livro.id_aluno = Aluno.id WHERE NOME = :nome")
        rs = con.execute(sql_consulta, {"nome": nome})
        colunas = ["id_livro", "id_aluno", "descricao"]
        resultado = []
        while True:
            result = rs.fetchone()
            if result is None:
                break
            d_result = {coluna: valor for coluna, valor in zip(colunas, result)}
            resultado.append(d_result)
        return resultado
