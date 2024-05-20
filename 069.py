idade = 0
homem = 0
mmenos = 0
while True:
    sexo = input('Qual o seu sexo? [M/F]:')
    
    i = int(input('Qual sua idade? '))
    if sexo in 'Ff':
        homem +=1
    if i > 18:
        idade+=1
    if sexo in 'Mm':
        if i < 20:
            mmenos+=1
    continuar = input('Quer continuar? [S/N]')
    if continuar in 'Nn':
        break
print(f'{idade} pessoa(s) tem mais de 18 anos, foram cadastrado {homem} homens e {mmenos} mulhere(s) com menos de 20 anos.')