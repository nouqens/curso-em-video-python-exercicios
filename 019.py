from random import choice
n1 = input('escolha um nome: ')
n2 = input('escolha outro nome: ')
n3 = input('escolha outro nome: ')
n4 = input('escolha outro nome: ')
l= n1,n2,n3,n4
print(f'O aluno sorteado é {choice(l)}.')