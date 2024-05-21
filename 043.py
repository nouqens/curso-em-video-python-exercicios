p= float(input('seu peso: '))
a= float(input('sua altura em metros: '))
i= p/(a**2)
print(i)
if i < 18.5:
    print('abaixo do peso.')
elif i <=25:
    print('peso ideal.')
elif i <= 30:
    print('sobrepeso.')
elif i <= 40:
    print('obesidade.')
elif i > 40:
    print('obesidade morbida.')