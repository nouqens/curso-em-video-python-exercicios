n = int(input('Escolha um numero: '))
e = int(input('Agora escolha um para converter seu numero : 1- binario; 2- octal; 3- hexadecimal: '))
b = bin(n)
b2 = oct(n)
b3= hex(n)
if e == 2:
   print(f'seu numero em octal é {b2}')
elif e == 1:
   print(f'seu numero em binario é {b}')
elif e == 3:
   print(f'seu numero em hexadecial é {b3}')