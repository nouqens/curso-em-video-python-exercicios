listagem = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32, 'Canetas',
            22.30, 'Livro', 34.90)
q = 0
qq = 1
print('-'*47)
print('                 LISTAGEM')
print('-'*47)
for n in range(9):
    print(f' {listagem[q]:.<30} R$  {listagem[qq]:>10.2f}')
    q+=2
    qq+=2
print('-'*47)