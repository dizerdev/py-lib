import requests

nome = input("Digite o nome: ")
sexo = input("Digite o sexo: ")
cabelo = input("Digite a cor do cabelo: ")

dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

pedido = requests.post("http://localhost:5002/pessoa", json=dados)
if pedido.status_code != 200:
    print(f"[{pedido.status_code}] {pedido.text}")
else:
    print(pedido.text)
