from math import trunc
f = input('Digite a Frase').lower().split()
j = ''.join(f)
t = len(j)
a = 0
for c in range(0, trunc(len(j) / 2)):
    if j[c] != j[t - 1]:
        a += 1
    t = t - 1
if a == 0:
    print('É um palindromo')
else:
    print('Não é um palindromo')
