def decorador(f):
    def envelope():
        print('código executado antes de chamar f')
        f()
        print('código executado apos de chamar f')
    return envelope


def decorador_turbo(f):
    def envelope(p1):
        print('código executado antes de chamar f')
        retorno = f(p1)
        print('código executado apos de chamar f')
        return retorno
    return envelope


@decorador
def ola_mundo():
    print('olá mundo')


# decorador de funcao
novo_decor = decorador(ola_mundo)
print(novo_decor())
