t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
s = 1
print('{}, '.format(t),end='')
while c != 10:
    t += r
    print(t,', ',end='')
    c += 1
    s += 1
print('PAUSA')
while c != 0:
    c = int(input('quantos termos você quer mostrar a mais? '))
    for a in range(0,c):
        t += r
        print(t, ', ', end='')
        s += 1
    print('PAUSA')
print('{} termos mostrados'.format(s))