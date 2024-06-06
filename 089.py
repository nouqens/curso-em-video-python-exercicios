matriz =list()
while True:
    nome= (input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = float((nota1+nota2)/2)
    matriz.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar? [S/N]: ')
    if continuar in 'Nn':
        break

print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
for x, y in enumerate(matriz):
    print(f'{x:<4}{y[0]:<10}{y[2]:>8}')
while True:
    verNota = int(input('Quer ver a nota de qual aluno? [999 interrompe]: '))
    if verNota == 999:
        print('Finalizando...')
        break
    if verNota <= len(matriz)-1:
        print(f'O nome é {matriz[verNota][0]} e suas notas são {matriz[verNota][1]}.')
    else:
        print('ALUNO NÃO ESTÁ NA LISTA!')