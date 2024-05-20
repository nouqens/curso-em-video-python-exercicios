n1= int(input('digite um numero: '))
n2= int(input('digite um segundo numero: '))
n3= int(input('digite um terceiro numero: '))
m= n1
ma= n1
if n2<n1 and n2<n3:
    m= n2
if n3<n1 and n3<n2:
    m= n3
print(f'o menor valor é {m}')
if n2>n1 and n2>n3:
    ma= n2
if n3>n1 and n3>n2:
    ma= n3
print(f'o maior valor é {ma}')
