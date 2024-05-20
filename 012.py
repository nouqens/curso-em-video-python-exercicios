#Faça um algoritmo que leia o preço de um produto a mostre seu novo preço. com 5% de desconto.
p1= int(input('diga um preço para um produto: '))
p2= int(p1 - (p1/100) * 5)
print(f'{p2}')
