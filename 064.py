a = 0
b = 0
d = 0
while a != 999:
    a = int(input("Digite um numero de 0 a 999: "))
    if a != 999:
        b+=a
    else:
        c = b+0
    d+=1
print(f'a soma total dos numeros digitados foi de {b} e a quantidades de tentativas foram {d}.')    
