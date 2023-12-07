def incrementa_int(n):
    print('função incrementa_int: n -', n)
    if not isinstance(n, int):
        raise TypeError('n deve ser um inteiro')
    return n + 1


def calcula_idade(idade):
    try:
        nova_idade = incrementa_int(idade)
    except Exception:
        print('Fazendo registro em ferramenta de log')
        raise
    else:
        print('esse código não é executado se der erro na linha acima')
        return nova_idade


def main():
    print('executando a função principal...')
    try:
        resposta = calcula_idade("20")
    except Exception:
        print('tente novamente')
    else:
        print('esse código não será executado se der erro na linha acima')
        print('a nova idade é:', resposta)


if __name__ == '__main__':
    print('chamando a função principal')
    main()
    print('esse código não será executado se der erro na linha acima')

# erro tratado com interceptação
