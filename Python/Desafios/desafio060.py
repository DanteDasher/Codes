n = t = int(input('Digite o numero para calcular o seu fatorial'))
r = 'Calculando fatorial de: ' + str(n) + ' = ' + str(n)
while n != 1:
    n = n - 1
    t = t * n
    r = r + ' X ' + str(n)
print(r,' = ',t)