lista = [0, 1, 2, 3]


def teste():
    def funcao_interna():
        return 'olá mundo'
    return funcao_interna


r = teste()
print(r())


def converte_2(f, sequencia):
    convertidos = []
    for item in sequencia:
        convertidos.append(f(item))
    return convertidos


# Passar a função raiz do python como parametro
lista_convertida = converte_2(str, lista)
print(lista_convertida)


def converte(tipo, sequencia):
    convertidos = []
    if tipo == "str":
        for item in sequencia:
            convertidos.append(str(item))
    if tipo == "int":
        for item in sequencia:
            convertidos.append(int(item))
    if tipo == "float":
        for item in sequencia:
            convertidos.append(float(item))
    else:
        raise Exception('Tipo não reconhecido')

    return convertidos


# Passar a função raiz do python como parametro
lista_convertida = converte_2(str, lista)
print(lista_convertida)
