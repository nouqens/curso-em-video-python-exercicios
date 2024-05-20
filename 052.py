n = int(input('digite um numero: '))
b = 0
for a in range(1, n+1):
    if n%a==0:
        b +=1
if b == 2:
    print('é primo')
else:
    print('não é primo')