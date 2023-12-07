# Escrevendo texto
texto = 'escrevendo a primeira frase \n'
texto2 = 'mais uma linha para esse texto \n'
with open('teste2.txt', 'w', encoding='utf-8') as f:
    f.write(texto + texto2)

# Escrevendo lista
s = [
    'linha 1 \n',
    'linha 2 \n',
    'linha 3 \n',
    'linha 4 \n'
]
with open('teste2.txt', 'a', encoding='utf-8') as f:
    f.writelines(s)

# Escrevendo uma f'str'
texto2 = texto + '\n'
s2 = [f'{linha}' for linha in s]
with open('teste2.txt', 'w') as f:
    f.write(texto2)
    f.writelines(s2)

# Escrevendo com print (opção file)
with open('teste2.txt', 'a', encoding='utf-8') as f:
    print(texto, file=f)
    for linha in s:
        print(linha, file=f)
