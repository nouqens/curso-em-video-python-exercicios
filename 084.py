matriz = []
principal = []
maior = menor = 0
while True:
    matriz.append(input('Qual o seu nome? '))
    matriz.append(float(input('Seu peso: ')))
    if len(principal) == 0:
        maior = menor = matriz[1]
    else:
        if matriz[1] > maior:
            maior = matriz[1]
        if matriz[1] < menor:
            menor = matriz[1]
    principal.append(matriz[:])
    matriz.clear()
    b = input('Quer continuar? [s/n] ')
    if b in 'nN':
        break

print(f'voce cadastrou {len(principal)} pessoas.')
print(f'o maior peso foi {maior}kg, de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'o menor peso foi {menor}kg, de ', end='')
for ps in principal:
    if ps[1] == menor:
        print(f'[{ps[0]}] ', end='')