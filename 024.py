#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
n = input('Digite o nome de sua cidade: ')
b = n.upper()
cc= b.split()
a = 'SANTO' in cc[0]
print(f'A nome da sua cidade comeca com santo? {a}')