l = []
for x in range(6):
    a= int(input())
    c= a%2
    if c == 0:
        l.append(a)
s= sum(l)
print(f'a soma do numeros pares é {s}')

