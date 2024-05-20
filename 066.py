n = s = cont = 0
while True:
    n = int(input('Um Número (999 para parar): '))
    if n != 999:
        s+=n
        cont+=1
    else:
        break
print(f'A quantidade de numeros digitados é {cont} e a soma dos mesmo é {s}.')
    