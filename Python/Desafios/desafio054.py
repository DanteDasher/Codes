from datetime import date
me = 0
ma = 0
for c in range(0,7):
    a = int(input('Ano de Nascimento: '))
    if date.today().year - a < 21:
        me += 1
    else:
        ma += 1
print('{} são Maiores e {} são menores'.format(ma,me))