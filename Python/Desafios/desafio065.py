n = int(input('Digite um número'))
ma = me = t = n
c = 1
v = True
while v == True:
    l = input('Deseja continuar? [S/N]').upper()
    if l == 'S':
        n = int(input('Digite um número'))
        if n > ma:
            ma = n
        elif n < me:
            me = n
        c += 1
        t += n
    elif l == 'N':
        t = t / c
        v = False
    else:
        print('incorreto, tente novamente')
print('Voce digitou {} números e a média foi: {} \nMaior número: {} \nMenor Numero: {}'.format(c,t,ma,me))