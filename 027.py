#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nom= str(input('digite seu nome completo: ')).strip()
b= nom.split()
print(f'seu primeiro nome é {b[0]} e seu ultimo nome é {b[-1]}')
