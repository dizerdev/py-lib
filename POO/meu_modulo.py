# para chamar modulo no terminal
# sintaxe py .\meu_modulo.py
def exibe_nome():
    print(f'O nome deste modulo é: {__name__!r}')


# Usual, utilizar essa sintaxe para
# visualizar se esse modulo é o principal
# e para testar o modulo
if __name__ == '__main__':
    print('Olá')
    nome = input('Digite seu nome: ')
    exibe_nome()


def soma_2(numero):
    return numero * 2
