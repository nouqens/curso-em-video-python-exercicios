r1 = float(input('valor da 1° reta: '))
r2 = float(input('valor da 2° reta: '))
r3 = float(input('valor da 3° reta: '))
v1= r1 + r2 >= r3 and r2 + r3 >= r1 and r3 + r1 >= r2
if v1 == True:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')