# tipos de dados

num_int = int(20)

char_str = str('Diego')

num_real = float(5000.0)

bool_flag = True

if bool_flag:

    print(f'{char_str} tem {num_int} anos e R${num_real} na conta')

# funções


def dobra(x):
    return 2 * x


def triplicar(x):
    triplo = 3 * x
    return triplo


n1 = float(input('Digite seu salário: '))
dobro = dobra(n1)
print(f'O dobro de {n1} é {dobro}')
print(f'O triple de {n1} é {triplicar(n1)}')
