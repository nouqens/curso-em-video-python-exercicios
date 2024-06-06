dict = {}
l = []
soma = media = 0
while True:
    dict.clear()
    dict['nome'] = str(input('Nome: '))
    while True:
        dict['sexo'] = str(input('Sexo; ')).upper()[0]
        if dict['sexo'] in 'MF':
            break
        print('DIGITE APENAS M OU F!')
    dict['idade'] = int(input('Idade:'))
    soma += dict['idade']
    l.append(dict.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('DIGITE APENAS S OU N!')
    if continuar == 'N':
        break

print(f'Ao todo foram cadastradas {len(l)} pessoas.')
media = soma / len(l)
print(f'A media de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ', end = '')
for x in l:
    if x['sexo'] == 'F':
        print(f'{x["nome"]} ', end = '')
print()
print('As pessoas acima da media são:')
for x in l:
    if x['idade'] >= media:
        print(f'nome = {x['nome']}; sexo = {x['sexo']}; idade = {x['idade']}')
print('<<ENCERRADO>>')