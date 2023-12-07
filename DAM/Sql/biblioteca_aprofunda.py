from sqlalchemy import create_engine
from sqlalchemy.sql import text

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///biblioteca.db')


def criar_tabelas():
    with engine.connect() as con:
        create_tabela_aluno = text("CREATE TABLE IF NOT EXISTS Aluno (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, email TEXT NOT NULL UNIQUE)")
        rs = con.execute(create_tabela_aluno)
        create_tabela_livro = text("CREATE TABLE IF NOT EXISTS Livro (id_livro INTEGER PRIMARY KEY, id_aluno INTEGER, descricao TEXT NOT NULL, FOREIGN KEY(id_aluno) REFERENCES Aluno(id))")
        rs = con.execute(create_tabela_livro)
    # essa constraint é uma boa, mas o SQLite está ignorando. Em bancos mais sofisticados, (como MySQL e Postgres) ela impede que haja livro com id_aluno invalida. id_aluno pode ser null, mas se tiver algum valor, o valor tem que ser válido


def criar_alunos():
    with engine.connect() as con:

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com')")
        rs = con.execute(add_aluno)

        add_aluno = text("INSERT INTO Aluno (id,nome,email) VALUES (4,'Diego', 'testedodiego@teste.com.br')")
        rs = con.execute(add_aluno)


def criar_livros():
    with engine.connect() as con:
        add_livro = text("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1, 1, 'Python completo e total')")
        rs = con.execute(add_livro)

        add_livro = text("INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias póstumas de brás cubas')")
        rs = con.execute(add_livro)

        add_livro = text("INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')")
        rs = con.execute(add_livro)

        add_livro = text("INSERT INTO Livro (id_livro, descricao) VALUES (4,'Algoritmos')")
        rs = con.execute(add_livro)


# Podemos executar a função criar livros várias vezes?
# NAO, ocasiona um erro, por violar a constraint de unicidade

# Podemos executar a função criar tabelas várias vezes?
# SIM, porque o comando usado é create table SE ELA NAO EXISTIR


def todos_alunos_one():
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
    # fetchone pega respectivamente uma linha do resultado
        # fetchone pode ser ineficiente por fazer muitos acessos ao disco rigido (pois o disco rigido é muito mais lento que a RAM, onde ficam as variáveis normais)


def todos_alunos_all():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados_sujo = rs.fetchall()
        resultados_limpo = []
        colunas = ["id", "nome", "email"]
        # print(resultados_sujo)
        for resultado in resultados_sujo:
            lista = []
            for i in resultado:
                lista.append(i)
            d_result = {coluna: valor for coluna, valor in zip(colunas, resultado)}
            resultados_limpo.append(d_result)
        print(resultados_limpo)
    # fetchall pega todas as linhas do resultado
        # fetchall pode ser ineficiente por carregar dados demais para a RAM, impedindo o servidor de processar outras demandas


def todos_alunos_many():
    with engine.connect() as con:
        sql_consulta = text("SELECT * FROM aluno")
        rs = con.execute(sql_consulta)
        resultados_sujo = rs.fetchmany(2)
        resultados_limpo = []
        colunas = ["id", "nome", "email"]
        # print(resultados_sujo)
        for resultado in resultados_sujo:
            lista = []
            for i in resultado:
                lista.append(i)
            d_result = {coluna: valor for coluna, valor in zip(colunas, resultado)}
            resultados_limpo.append(d_result)
        print(resultados_limpo)
    # fetchmany(20) pega numero de linhas passada por parametro
