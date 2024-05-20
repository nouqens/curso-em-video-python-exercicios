sb= int(input('o salario de jose é: '))
if sb<=1250:
    s10 = (sb/100)*15+sb
    print(f'seu aumento foi de 15% e agora é {s10}.')
else:
    s15= (sb/100)*10+sb
    print(f'seu aumento foi de 10% e agora é {s15}.')