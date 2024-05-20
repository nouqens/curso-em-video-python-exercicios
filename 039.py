nas = int(input('Qual você nasceu? '))
i = 2024-nas
if i < 18:
    t = 18-i
    print(f'Você ainda vai se alistar no serviço militar, falta(m) {t} anos ainda.')
elif i == 18:
    print('Está na hora de se alistar no serviço militar.')
elif i > 18:
    tt= i-18
    print(f'Já passou a hora de se alistar no serviço militar, exatamente {tt} anos.')