c = r = n = 0

while n != 999:
    n = int(input('Digite um numero(999 para parar)'))
    r += n
    c += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(c - 1, r - 999))