dic = {
    "alimentos": {
        "pizzas": ["margueritta", "mussarella",
                   "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra",
                  "red velvet",
                  "de laranja", "dá vó"),
        "calorias": {
            "leite": 129, "fatia pizza": 320,
            "agua": 0, "maça": 95
            }
    },
    "linguagens": [
        {"nome": "javascript", "criacao": 1996,
         "paradigma": ["eventos", "funcional"]},
        {"nome": "python", "criacao": 1991,
         "paradigma": ["orientada a objetos", "estruturada"]},
        {"nome": "haskell", "criacao": 1990,
         "paradigma": ["funcional"]}
        ]
    }


def exercicios(dic):
    # Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
    # Se possível, FAÇA JUNTO NO SEU COMPUTADOR

    # 1. quantas chaves tem o dicionario dic?
    print("r1", len(dic))

    # 2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
    print("r2", type(dic["linguagens"]))


    # 3. Como eu faço para mostrar todos os bolos?
    print("r3", dic["alimentos"]["bolos"])


    # 4. Qual o tipo da lista de todos os bolos?
    print("r4", type(dic['alimentos']['bolos']))


    # 5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # R: O erro foi o exemplo querer acessar uma lista de forma invalida, o tipo do erro é: TypeError: string indices must be integers, not 'str'
    print("r5", dic["linguagens"][0]["paradigma"][0])


    # 6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # R não exite erro de execução mas a busca é de forma errada, para corrigir deve acessar o valor "haskell" pela chave ["nome"]
    print("r6", dic["linguagens"][2]["nome"] == "haskell")


    # 7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # R Para o valor mussarela ser exibido, o codigo deve buscar no indice correto, que seria o indice [1] dentro da lista "pizzas"
    print("r7", dic["alimentos"]["pizzas"][1] == "mussarella")


    # 8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # R A busca do in em um dicionario busca por chaves e não por valores, para corrigir o erro deve ser utilizado a função values()
    print("r8", 1996 in dic["linguagens"][0].values())


    # 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # Não gera nenhum erro, por a sintaxe está correta
    print("r9", "criacao" in dic['linguagens'][0])


    # 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
    # R Para corrigir o erro por que não existem a chave "sobremesas" dentro de dic
    print("ex9b", "pudim" in dic["sobremesas"]["doces"])


    # 10 Escreva uma função "mais velha" que recebe um dicionário como dic e retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista


def mais_velha(dic):
    # construtora
    lista_linguagens = dic["linguagens"]
    # Inicializadora
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        # comparação entre valores
        if linguagem["criacao"] < ling_velha["criacao"]:
            # atribuição à inicializadora
            ling_velha = linguagem
    # retorno da inicializadora
    return ling_velha


    # 11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação
    # Para eliminar as repetições neste exemplo, é necessario verificar através do not in se o valor do p nunca apareceu em paradigmas, se já apareceu ele adiciona, se não ele não adiciona


def todos_paradigmas(dic):
    # construtora
    lista_linguagens = dic["linguagens"]
    # inicializadora
    paradigmas = []
    for linguagem in lista_linguagens:
        # criar lista com os paradigmas de cada linguagem
        paradigmas_da_linguagem = linguagem["paradigma"]
        # para cada elemento da lista com os paradigmas
        for p in paradigmas_da_linguagem:
            # adicionar esse elemento na lista inicializadora
            if p not in paradigmas:
                paradigmas.append(p)
    return paradigmas


print(todos_paradigmas(dic))
