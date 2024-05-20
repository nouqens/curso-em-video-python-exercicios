l = []
for a in range(5):
    b = int(input('seu peso: '))
    l.append(b)
l.sort()
print(f'{l[0]} foi o menor peso e {l[4]} o maior peso')