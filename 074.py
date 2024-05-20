from random import randint
numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100), randint(0,100))
print('o numeros sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\no maior numero é: {max(numeros)}')
print(f'o menor numero é: {min(numeros)}')