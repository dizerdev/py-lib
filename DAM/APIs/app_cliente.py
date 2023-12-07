import requests
from pprint import pprint


def todos_corredores():
    url = 'http://localhost:5000/corredores'
    pedido = requests.get(url)
    resposta = pedido.json()
    return resposta


def adiciona_corredor(nome, tempo, id):
    url = 'http://localhost:5000/corredores'
    corpo = {"nome": nome, "tempo": tempo, "id": id}
    pedido = requests.post(url, json=corpo)
    return pedido


def corredor_mais_lento():
    url = 'http://localhost:5000/corredores/maior_tempo'
    pedido = requests.get(url)
    resposta = pedido.json()
    return resposta


# toda vez que é chamada, a função pop() faz deletar um registro
def deleta_mais_lento_vulneravel():
    url = 'http://localhost:5000/corredores/maior_tempo'
    pedido = requests.delete(url)
    if pedido.status_code == 500:
        return 'não é possivel remover de uma lista vazia'
    return 'Ok'


# assim somente registro passado por parametro vai sofrer o pop()
def deleta_mais_lento_correto(id_deletar):
    url = f'http://localhost:5000/corredores/{id_deletar}'
    pedido = requests.delete(url)
    if pedido.status_code == 404:
        return 'o registro já não existe mais'
    return 'Ok'


def corredor_por_id(id_corredor):
    url = f'http://localhost:5000/corredores/{id_corredor}'
    pedido = requests.get(url)
    if pedido.status_code == 404:
        return 'O corredor não foi encontrado'
    resposta = pedido.json()
    nome = resposta['corredor']['nome']
    tempo = resposta['corredor']['tempo']
    return (nome, tempo)


def deletar_por_id(id_corredor):
    url = f'http://localhost:5000/corredores/{id_corredor}'
    pedido = requests.delete(url)
    if pedido.status_code == 404:
        return 'O corredor não foi encontrado'
    return 'ok'


def novo_tempo(id_corredor, tempo):
    url = f'http://localhost:5000/corredores/{id_corredor}'
    pedido = requests.put(url, json={"tempo": tempo})
    if pedido.status_code == 400:
        return "Tempo nao atualizado por ser maior que o record"
    if pedido.status_code == 404:
        return "Corredor não encontrado"
    return "ok"
