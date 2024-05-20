n1= float(input('Qual sua nota parcial? '))
n2= float(input('Qual sua nota bimestral? '))
nf= (n1+n2)/2
if nf<5:
    print(f'Você foi reprovado.')
elif nf>5 and nf<6.9: 
    print('Você ficou de recuperação.')
else:
    print('PARABÉNS, VOCÊ FOI APROVADO!!!')
