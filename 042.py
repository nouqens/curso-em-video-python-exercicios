r1= float(input('valor da 1° reta: '))
r2= float(input('valor da 2° reta: '))
r3= float(input('valor da 3° reta: '))
v = r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2
if r1 == r2 and r1 == r3 and r2 == r3:
    print('forma um triangulo equilatero.')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('forma um triangulo isoseles.')
else:
    print('forma um triangulo escaleno.')