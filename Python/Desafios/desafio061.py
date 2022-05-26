t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
print('A progreção é: {}'.format(t),end='')
while c != 10:
    t += r
    print(', ',t,end='')
    c += 1
