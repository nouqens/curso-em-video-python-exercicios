ns=  int(input('Vc nasceu em qual ano? '))
i = 2024-ns
if i<=9:
    print('Voce esta no rank mirim em competições de natação.')
elif i<=14:
    print('vc esta no rank infantil em competições de natação.')
elif i<=19:
    print('vc esta no rank junior em competições de natação.')
elif i==20:
    print('vc esta no rank sênior em competições de natação.')
else:
    print('vc esta no rank master em competições de natação.')