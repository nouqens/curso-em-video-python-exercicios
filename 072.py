numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    a = int(input('digite um numero entre 0 e 10: '))
    if 0 <= a <=10:
        break
    print('tente novamente... ', end='')
print(f'o numero que vc digitou é {numeros[a]}.')