n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero: '))
ma = n1
me = n1
if(n2 > ma):
    ma = n2
else:
    me = n2

if(n3 > ma):
    ma = n3

if(n3 < me):
    me = n3

print('o maior valor é : {} e o menor é: {}'.format(ma,me))