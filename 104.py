def leiaint(msg):
    valor = 0
    while True:
        num = str(input(msg))
        try:
            num.isnumeric()
            valor = int(num)
            break
        except:
            print(f'\033[0;31mERRO: "{num}" é um numero inteiro invalido\033[m')
        
    return valor

def leiareal(msg):
    valor = 0
    while True:
        num = str(input(msg))
        try:
            num.isdecimal()
            valor = float(num)
            break
        except:
            print(f'\033[0;31mERRO: "{num}" é um numero real invalido\033[m')
        
    return valor


n = leiaint('Digite um numero inteiro: ')
print(f'voce digitou o numero inteiro {n}')
nn = leiareal('Digite um numero real: ')
print(f'O numero real digitado é {nn}')