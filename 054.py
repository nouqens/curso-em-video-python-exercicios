ma = 0
me = 0
for c in range(7):
    n = int(input('seu ano de nascimento: '))
    i = 2024-n
    if i<21:
        me+=1
    else:
        ma+=1
print(f'{ma} são maiores de idade e {me} são menores de idade.')