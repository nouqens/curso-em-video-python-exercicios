import random
n = random.randint(0,10)
n1 = 1
a = int(input('Digite um numero: '))
while a != n:
    a = int(input('Digite um numero: '))
    n1 += 1
print(f'Voce ganhou com {n1} chances.')
