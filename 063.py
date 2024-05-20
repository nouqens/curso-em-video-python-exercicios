num = int(input('Digite um numero: '))
fn = 0
fn2 = 1
q = 3
print(fn, end=" => ")
print(fn2, end=" => ")
while q <= num:
    t3 = fn+fn2
    fn = fn2
    fn2 = t3
    q+=1
    print(t3, end=" => ")