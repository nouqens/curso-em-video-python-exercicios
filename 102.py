def fatorial(a=1):
    import time
    f = 1
    for c in range(a, 0, -1):
        f*=c
    return f


num = fatorial(int(input('Digte um número: ')))
print(f'o fatorial é {num}')