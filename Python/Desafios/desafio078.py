ln = list()
ma = 0
me = 0
for c in range(0,5):
    ln.append(int(input(f'Digite o valor da posição {c} ')))
    if c == 0:
        me = ln[c]
    elif ln[c] < me:
        me = ln[c]
    if ln[c] > ma:
        ma = ln[c]
print(f'Você digitou os valores{ln}')
print(f'O maior valor digitado foi {ma} nas posições ',end='')
for c,n in enumerate(ln):
    if ma == n:
        print(c,end='...')
print(f'\nO menor valor digitado foi {me} nas posições ',end='')
for c,n in enumerate(ln):
    if me == n:
        print(c,end='...')