from random import choice
n1 = choice([0,1,2,3,4,5])
n2 = int(input('O computador pensou em um numero entre 0 e 5, adivinhe qual é: '))
if(n1 == n2):
    print('Ganhou!!!')
else:
    print('Perdeu!!! o numero é: {}'.format(n1))
