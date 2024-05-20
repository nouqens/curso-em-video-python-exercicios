from random import randint
nj = 0
nc = randint(1,10)
v = 0
print('=-=-=-=-=-=-=-=-=-=-=-=-= \n      PAR OU IMPAR!\n =-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
    nj = int(input('Digite um valor: '))
    es = str(input('Par ou Impar? [P/I]: '))
    b = (nj+nc)
    if es in 'Pp':
        d = b%2
        if d == 0:
            print(f'Deu par, porque seu numero ({nj}) mais o do computador ({nc})! E vc ganhou!')
            print('Vamos jogar novamente...')
            v +=1
        else:
            print(f'Deu impar, porque seu numero ({nj}) mais o do computador ({nc})! E vc perdeu!')
            break
    if es in 'Ii':
        e = b%3
        if e == 0:
            print(f'Deu impar, porque seu numero ({nj}) mais o do computador ({nc})! E vc ganhou!')
            print('Vamos jogar novamente...')
            v+=1
        else:
            print(f'Deu par, porque seu numero ({nj}) mais o do computador ({nc})! vc perdeu!')
            break
if v == 0:
    print(f'Voce não venceu!')
if v > 0:
    print(f'Voce {v} vezes!')