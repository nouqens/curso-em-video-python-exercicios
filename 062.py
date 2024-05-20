t1 = int(input('o primeiro termo: '))
r = int(input('digite a razao: '))
b = 1
c = t1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while b <= total:
        b+=1
        c+=r
        print(c)
    mais = int(input('mais quantas pa? '))
print('=-' * 20)
print('         FIM')
print(f'o total de PAs foi de {total}')