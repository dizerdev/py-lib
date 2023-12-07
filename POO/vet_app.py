from paciente import Paciente, NameIsEmptyError

try:
    nome = input('Digite o nome do paciente: ')
    p = Paciente(nome)
except TypeError:
    print('O nome deve ser uma string. Tente novamente...')
except NameIsEmptyError:
    print('O nome não pode ser uma string vazia, preencha um valor...')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto de Paciente')
    print('informações do erro', e)
else:
    print('Agora está tudo certo.')
finally:
    print('Sempre será executado')
