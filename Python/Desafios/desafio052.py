n = int(input('Numero: '))
p = 0
for c in range(n, 0, -1):
    if n % c == 0:
        p += 1
if p <= 2 :
    print('{} é um numero Primo'.format(n))
else:
    print('{} Não é numero Primo'.format(n))