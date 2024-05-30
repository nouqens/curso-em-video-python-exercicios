matriz = [[], []]
for x in range(7):
    p = (int(input('Digite um numero: ')))
    if p %2 == 0:
        matriz[0].append(p)
    else:
        matriz[1].append(p)

print(f'os pares são {sorted(matriz[0])}')
print(f'os impares são {sorted(matriz[1])}')