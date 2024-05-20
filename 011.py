#Faça um programa que leia a largura a a altura de uma parada em metros, calcule a sua uma área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². DDDDJU
l= int(input('digite a largura de uma parede: '))
h= int(input('digite a altura de uma parede: '))
a= l*h
qt= int(a/2)
print(f'a area da parede é de {a}m e a quantidade tintas que serão ultilzidas é {qt}.')