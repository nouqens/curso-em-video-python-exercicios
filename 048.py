l = []
for c in range(500):
    b = c%2
    if b == 1:
        j = c%3
        if j == 0:
            l.append(c)
print(sum(l))