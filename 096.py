def area(*lst):
    a = lst[0]*lst[1]
    print(f'a area do terrono {lst[0]:.1f}x{lst[1]:.1f} é igual a {a}m².')
print(f'{'CONTROLE DE TERRENO':>15}')
print('-'*30)
l, h = float(input('Largura: ')), float(input('Altura: '))
area(l, h)
