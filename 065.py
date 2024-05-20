num = int(input('digite um numero: '))
l = []
total = 1
a = 0
mais = 1
while mais != 0:
    total = total + mais
    while a != num:
        a+=1
        num = int(input('digite um numero: '))
        l.append(num)
    mais = int(input('mais quantos numeros? '))
b = l.sort(reverse=True)
print(f'o maior numero é {l[0]}')
c = l.sort()
print(f'o menor numero é {l[0]}')
d = (sum(l))/total
print(f'a media foi de {d}')
