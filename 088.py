import random, time
n = int(input('Numero de jogos: '))
print(f'=-=-=-=-=-=-=-=-=SORTEADO {n} JOGOS=-=-=-=-=-=-=-=-=')
for x in range(n):
    ns = random.sample(range(1, 61), 6)
    print(f'jogo {x+1} = {sorted(ns)}')
    time.sleep(0.75)