import csv

colunas = ['Descrição', 'Potência (Watts)', 'Tensão (Volts)',
           'Quantidade em estoque', 'Preço (R$)']
estoque = [
    ['Liquidificador 5 velocidades', 800, 220, 8, 259.99],
    ['Geladeira 350 litros', 75, 110, 4, 1372.99],
    ['Microondas 20 litros', 1500, 220, 21, 499.99],
]

# Escrevendo arquivo especificado CSV
with open('estoque.csv', 'w', newline='',
          encoding='UTF-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(colunas)
    escritor.writerows(estoque)

# Lendo arquivo csv e criando objeto para
with open('estoque.csv', 'r', newline='',
          encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    novo_estoque = []
    for linha in leitor:
        novo_estoque.append(linha)
    print(novo_estoque)

# Desenpacotando o arquivo csv
novas_colunas, *novo_estoque = novo_estoque
print(novas_colunas)
print('[', *novo_estoque, sep='\n  ', end='\n]')
