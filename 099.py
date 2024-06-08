from time import sleep
'''def maior(*num):
    tam = len(num)
    l = []
    
    print('Analisando Valores...')
    sleep(1)
    for x in num:

        print(f'{x} ',end= '')
        sleep(0.5)
        l.append(x)
    print()
    print(f'foram informados {tam} numeros ')
    print(f'o maior valor foi {max(l)}.')

maior(6,7,8,9,10)
maior(4,7,0)
maior(1,2)
maior(6)
maior()'''
def maior(*num):
    cont = 0
    print('Analisando Valores...')
    sleep(0.35)
    for x in num:
        print(f'{x} ', end='')
        sleep(0.35)
        cont+=1
    print(f'foram informados {cont} valores.')
    if cont != 0:
        print(f'o maior valor foi {max(num)}')
    else:
        print(f'o maior valor foi 0.')

maior(6,7,8,9,10)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
