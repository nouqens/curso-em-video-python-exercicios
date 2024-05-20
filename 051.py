t1= int(input('digite o primeiro termo: '))
r= int(input('digite a razão: '))
d = t1 + (10 - 1) * r
for b in range(t1, d + r , r):
    print(b, end= ' -> ')