a = 0
while True:
    a = int(input("Qual numero voce quer ver a tabuada? "))
    if a >=0:
        print(f'a multiplicação de {a} é: \n {a} x 1 = {a*1}\n {a} x 2 = {a*2}\n {a} x 3 = {a*3}\n {a} x 4 = {a*4}\n {a} x 5 = {a*5}\n {a} x 6 = {a*6}\n {a} x 7 = {a*7}\n {a} x 8 = {a*8}\n {a} x 9 = {a*9}\n {a} x 10 = {a*10}')
    else:
        print('PROGRAMA ENCERRADO!')