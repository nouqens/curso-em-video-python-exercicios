def votar(i):
    from datetime import date
    idade = date.today().year-i
    print(f'com {idade} anos: ', end = '')
    if idade >=18:
        return "VOTAÇÃO OBRIGATORIA"
    elif 16 <= idade < 18 or idade >= 65:
        return "VOTAÇÃO OPICIONAL"
    else:
        return "NÃO VOTA"


r = votar(int(input("Ano de Nascimento: ")))
print(r)