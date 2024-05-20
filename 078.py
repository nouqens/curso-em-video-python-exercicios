l = []
for x in range(5):
    l.append(int(input('Digite um numero: ')))
print(f'o menor valor é {min(l)} e está nas posições: ', end=" ")
for y, b in enumerate(l):
    if b == min(l):
        print(f'{y}...', end =" ")
print()
print(f'o maior valor é {max(l)} e está nas posições: ', end='')
for i, v in enumerate(l):
    if v == max(l):
        print(f'{i}...', end =" ")