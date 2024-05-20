l = []
c = True
while c == True:
    a = int(input('Digite um numero: '))
    if a not in l:
        l.append(a)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! Numero nao adicionado!')
    b= input('Quer continuar? [s/n] ')
    if b in 'Ss':
        c = True
    else:
        c = False
l.sort()
print(f'voce digitou os valores: {l}')