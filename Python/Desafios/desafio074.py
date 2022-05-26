from random import randint
tn = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
ma = tn[0]
me = tn[0]
for c in range(1,5):
    if tn[c] > ma:
        ma = tn[c]
    if tn[c] < me:
        me = tn[c]
print(f'Numeros sorteados: {tn} \nMaior: {ma} \nMenor: {me}')
