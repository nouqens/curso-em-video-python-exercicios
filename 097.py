def tamanho(frase):
    tam = len(frase)
    print('~'*(tam+4))
    print(frase.center(tam+4))
    print('~'*(tam+4))
tamanho(input('Frase: '))