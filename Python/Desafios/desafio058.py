from random import randint
c = randint(0,10)
t = 1
print('Tente advinha o numero entre 0 e 10')
p = int(input('Digite o Numero:'))
while p != c:
    if p > c:
        p = int(input('Muito alto, tente um numero mais baixo'))
    elif p < c:
        p = int(input('Muito baixo, tente um numero mais alto'))
    t = t + 1
print('Parabens acertou era {} \nNumero de tentativas: {}'.format(c,t))