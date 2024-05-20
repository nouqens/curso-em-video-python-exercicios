from random import choice
n1= input('Primeiro aluno: ')
n2= input('segundo aluno: ')
n3= input('terceiro aluno: ')
n4= input('quarto aluno: ')
l= [n1,n2,n3,n4]
print(f'o escolhido foi {choice(l)}')