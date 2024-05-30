l = []
while True:
    a = int(input('Digite um número: '))
    l.append(a)
    b = input('Quer continuar? [s/n] ')
    while b not in 'nNsS':
        b = input('Resposta invalida! Use apenas s/n: ')
    if b in 'nN':
        break

print(l)
pares = [i for i in l if i%2 == 0]
impar = [j for j in l if j%2 != 0]
print(pares)
print(impar)