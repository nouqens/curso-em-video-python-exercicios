d= int(input('distancia da viagem: '))
p= d*0.5
ex= d-200
vr= (ex*0.45)
t= vr+p
if d<=200:
    print(f'sua viagem custou {p}')
else:
    print(t)