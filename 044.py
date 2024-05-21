p= float(input('Valor: '))
f= int(input('Escolha a forma de pagamento: 1- a vista'
' ou 2- cartao:'))
if f== 1:
    d10= p-(p/100*10)
    print(f'o valor com desconto de da 10% é {d10}')
elif f== 2:
    a = int(input('Em quantas vezes 1, 2, 3 ou mais vezes: '))
    if a== 1:
        d5= p-(p/100*10)
        print(f'o valor com desconto de 5% é {d5}')
    elif a == 2:
        print(f'nao tera desconto, ficando em {p}')
    elif a >= 3:
        au20= p+(p/100*20)
        print(f'o valor teve um aumento de 20% ficando em {au20}')
    
    