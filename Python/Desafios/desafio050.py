s = 0
for c in range(0,6):
    n = int(input('Digite um Valor: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos valores pares é {}'.format(s))