import requests


# solicita a entrada de dados para os testes
def entradaDados():
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    cabelo = input("Digite a cor do cabelo: ")

    dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

    return dados


# testando rota /pessoas 'POST'
def testePost():
    dados = entradaDados()
    # faz um request POST para a rota /pessoa (que aceita post)
    # passando o dicionario retornado pela função, para json
    pedido = requests.post("http://localhost:5002/pessoa", json=dados)
    # verifica se deu OK
    if pedido.status_code != 200:
        # printa parametro do objeto requests -status_code e -text(corpo)
        print(f"[{pedido.status_code}] {pedido.text}")
    else:
        # se não printa o -text(corpo) e BarRequest vindo do servidor
        print(pedido.text)


# testando rota /pessoas/<indice da lista> 'PUT'
def testePut():
    # atribui um valor inteiro a uma variavel id_pessoa
    id_pessoa = int(input('Digite o id da pessoa que deseja alterar: '))
    dados = entradaDados()
    # faz um request PUT para a rota /pessoas/<int:id_pessoa> que aceita PUT
    # passando a variavel id_pessoa que indica o indice da lista no servidor
    # e com um corpo da variavel dados em formato json
    pedido = requests.put("http://localhost:5002/pessoa/" +
                          str(id_pessoa),
                          json=dados)

    if pedido.status_code != 200:
        print(f"[{pedido.status_code}] {pedido.text}")
    else:
        print(pedido.text)


# testando rota /pessoas/<indice da lista> 'GET'
def testeGetId():
    # atribui um valor inteiro a uma variavel id_pessoa
    id_pessoa = int(input('Digite o id da pessoa que deseja buscar: '))
    # faz um request GET para a rota /pessoas/<int:id_pessoa> que aceita GET
    # passando a variavel id_pessoa que indica o indice da lista no servidor
    pedido = requests.get("http://localhost:5002/pessoa/" + str(id_pessoa))
    # se der qualquer coisa diferente de OK
    if pedido.status_code != 200:
        # printa status_code e corpo
        print(f"[{pedido.status_code}] {pedido.text}")
    # se der OK(200)
    else:
        # printa o text(corpo) do pedido
        print(pedido.text)


# testando rota /pessoas/<indice da lista> 'DELETE'
def testeDelete():
    # atribui um valor inteiro a uma variavel id_pessoa
    id_pessoa = int(input('Digite o id da pessoa que deseja excluir: '))
    # faz um request DELETE para a rota /pessoas/<int:id_pessoa>
    pedido = requests.delete("http://localhost:5002/pessoa/" + str(id_pessoa))
    if pedido.status_code != 200:
        print(f"[{pedido.status_code}] {pedido.text}")
    # se tudo ok retorna todo corpo restante
    else:
        print(pedido.text)


print('------------------------------------------\n')
print('Tentando a rota /pessoa com POST\n')
testePost()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com POST novamente \n')
testePost()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com PUT \n')
testePut()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com GET e pessoa específica\n')
testeGetId()

print('------------------------------------------\n')
print('Tentando a rota /pessoa com DELETE\n')
testeDelete()
