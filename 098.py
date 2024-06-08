from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 1, 2)
print(f'Agora é a sua vez!!!')
inicio, fim, passo = int(input('Inicio: ')), int(input('Fim: ')), abs(int(input('Passo: ')))
if passo == 0:
    passo = 1
contador(inicio, fim, passo)