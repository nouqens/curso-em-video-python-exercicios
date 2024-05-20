f = input('digite uma frase: ')
se = f.split()
aa= "".join(se)
a = aa [::-1]
if aa == a:
    print('é uma polindromio')
else:
    print('não é um polindromio')