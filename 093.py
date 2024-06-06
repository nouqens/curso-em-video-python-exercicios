dict = {}
l = []
dict["nome"] = str(input('Nome: '))
partidas = int(input('N° de partidas: '))
for x in range(partidas):
    l.append(int(input(f'gols da partida {x}: ')))

dict['gols'] = l[:]
dict['total'] = sum(l)
print('-=' * 30)
print(dict)
print('-=' * 30)
for k, v in dict.items():
    print(f'o campo {k} é igual a {v}.')
print('-=' * 30)
print(f'o jogador {dict["nome"]} jogou {len(dict["gols"])} partidas.')
for x in range(partidas):
    print(f'    na partida {x}, fez {l[x]} gols.')
print(f'foi um total de {dict["total"]} de gols.')
print('-=' * 30)
