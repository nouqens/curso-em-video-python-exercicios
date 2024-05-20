t = (int(input('digite um numero: ')),
     int(input('digite um numero: ')),
     int(input('digite um numero: ')),
     int(input('digite um numero: ')),
     int(input('digite um numero: ')))
print(f'o numero 9 apareceu {t.count(9)} vezes.')
if t.count(3) > 0:
    print(f'o numero 3 apareceu na posição {t.index(3)+1}° pela primeira vez.')
else:
    print('o numero 3 não apareceu em nenhuma posição.')
print('os numeros pares são: ', end='')
for n in t:
    if n%2 == 0:
        print(n, end=' ')