p = float(input('Primeira Nota: '))
s = float(input('Segunda Nota: '))
m = (p + s) / 2
if m >= 7 :
    print('Sua média foi: {}, você foi APROVADO'.format(m))
elif m < 5 :
    print('Sua média foi: {}, você esta de REPROVADO'.format(m))
else:
    print('Sua média foi: {}, você esta RECUPERAÇÃO'.format(m))
