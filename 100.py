from random import randint
from time import sleep
def sorteio():
    lst = []
    print(f'Sorteando 5 valos: ', end='', flush=True)
    sleep(0.3)
    while len(lst) < 5:
        a = randint(1, 10)
        if a not in lst:
            lst.append(a)
            print(a, end=' ', flush=True)
            sleep(0.3)
    sleep(0.3)
    print('Pronto!')
    return lst
numeros = sorteio()
def somaPar(lst):
    soma = 0
    for x in lst:
        if x % 2 == 0:
            soma += x
    sleep(1)
    print(f'a soma dos pares de {lst} é {soma}.')
somaPar(numeros)