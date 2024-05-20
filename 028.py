from random import randint
a = randint(0,5)
b = int(input('Digite um numero de 0 a 5 pare ser sorteado: '))
if a==b:
    print('Você ganhou!')
else:
    print(f'Você perdeu! O numero sorteado foi {a}')

