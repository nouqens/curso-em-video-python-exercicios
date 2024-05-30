l = []

while True:
    a = int(input('Digite um número: '))
    l.append(a)
    b = input('Quer continuar? [s/n] ')
    while b not in 'nNsS':
        b = input('Resposta invalida! Use apenas s/n: ')
    if b in 'nN':
        break

l.sort(reverse=True)

print(f'A quantidade de numeros digitados foi {len(l)}.')
print(f'A lista em ordem decrescente é {l}.')
print('O numero 5 está na lista!' if 5 in l else 'O numero 5 não esta na lista!')