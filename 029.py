v= int(input('Velocidade de um carro: '))
mt= (v-80)*7
if v <= 80:
    print('vc esta na velocidade permitida')
else:
    print(f'voce foi multado em R${mt:.0f} por ultrapassar os 80km/h.')