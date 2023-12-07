import json

aluno = {
    'nome': 'Paulo Ferreira',
    'ra': '001234567',
    'curso': 'ADS',
    'matriculado': True,
    'data_formatura': None,
    'disciplinas': [
        {
            'nome': 'Programação Orientada a Objetos',
            'notas_acs': [7, 8, 7.5],
            'nota_prova': 8,
        },
        {
            'nome': 'Desenvolvimento Web',
            'notas_acs': [10, 10, 7],
            'nota_prova': 9,
        },
        {
            'nome': 'Linguagem SQL',
            'notas_acs': [5, 9, 7.5],
            'nota_prova': 8.5,
        },
    ]
}


# Escrevendo a partir de uma string
aluno_str = json.dumps(aluno, indent=2)
print(aluno_str)


# Escrevendo novo arquivo json
with open('aluno.json', 'w') as f:
    json.dump(aluno, f, indent=2)


# Desenpacotando json a partir de uma string
aluno_carregado_da_string = json.loads(aluno_str)


# Lendo json a partir de um aquivo
with open('aluno.json', 'r') as f:
    aluno_carregado_do_arquivo = json.load(f)


# Comparando osa tipos
print('Comparação 1:', aluno_carregado_da_string == aluno)
print('Comparação 2:', aluno_carregado_do_arquivo == aluno)
