def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! digite um numero inteiro invalido!\033[m')
        else:
            return n


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! digite um numero inteiro invalido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario decidiu não informar os dados!\033[m')
            return 0
        else:
            return n


n = leiaint('Digite um numero inteiro: ')
print(f'voce digitou o numero inteiro {n}')
nn = leiareal('Digite um numero real: ')
print(f'O numero real digitado é {nn}')