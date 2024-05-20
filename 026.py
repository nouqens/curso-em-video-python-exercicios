#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fra= input('Digite uma frase: ')
sm= fra.strip()
aa= sm.upper()
con = aa.count('A')
pro= aa.find('A')+1
pra= aa.rfind('A')+1
print(f'A letra A aparece {con}.')
print(f'A letra A aparece pela primeira vez na posição {pro}.')
print(f'A letra A aparece pela última vez na prosição {pra}.')