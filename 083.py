ex = input()
parentese = []
for l in ex:
    if l == '(':
        parentese.append('(')
    elif l == ')':
        if len(parentese) > 0:
            parentese.pop()
        else:
            parentese.append(')')
            break
print('Sua expressão é valida!' if len(parentese) == 0 else 'Sua expressão é invalida! ')
