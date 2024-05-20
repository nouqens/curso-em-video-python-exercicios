n = input('Qual seu nome completo?  ')
k = n.upper()
m = n.lower()
sp= n.split()
s = ''.join(sp)
c = len(s)
cc= len(sp[0])
print(f'''Seu nome em totalemente em maiusculo é {k}; \n Seu nome em totalemente em minusculo é {m}; 
\n A quantidade de letras do seu nome sem contar os espaços é {c};  \n A quantidade de letras do seu primeiro nome é de {cc}.''')