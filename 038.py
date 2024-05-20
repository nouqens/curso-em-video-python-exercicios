n1 = int(input('Digite um número: '))
n2= int(input('Digite um segundo número: '))
if n1>n2:
    print(f'{n1} é o maior valor.')
elif n2>n1:
    print(f'{n2} é o maior valor.')
elif n1 == n2:
    print(f'Os números são iguais.')