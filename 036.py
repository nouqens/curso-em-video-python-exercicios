vc= int(input('Valor da casa que deseja comprar: '))
ss= float(input('Qual seu salario? '))
qt= int(input('Por quanto tempo deseja pagar a casa? '))
pr= (vc/qt)/12
vcs= (ss/100)*30+ss
if pr<vcs:
    print('Vc nao pode comprar a casa!')
else: 
    print('Vc pode comprar a casa!')