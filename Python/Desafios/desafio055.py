ma = 0
me = 0
for c in range(0,5):
    p = float(input('Peso '))
    if p > ma:
        ma = p

    if p < me:
        me = p

    if me == 0:
        me = p
print('O maior peso é {} e o menor peso é {}'.format(ma,me))