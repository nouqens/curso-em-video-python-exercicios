dict = {}
dict['nome'] = str(input('Nome: '))
dict['idade'] = 2024 - int(input('Nascimento: '))
aposento = 70 - dict['idade']
dict['ctps'] = int(input('Carteira de trabalho [0 se nao tem]: '))
if dict['cttps'] != 0:
    dict['contracao'] = int(input('Ano de contratação: '))
    dict['salario'] = int(input('Salario: '))
    dict['aposento'] = dict['idade'] + 35 + (2024 - dict['contracao'])

for k, v in dict.items():
    print(f' - {k} é igual a {v}')
