s = input('Digite seu sexo [F/M]').upper()
while s != 'F' and s != 'M':
    if s != 'F' and s != 'M':
        s = s.replace(s,input('Invalido, tente novamente [F/M]').upper())
print('Valor {} registrado com sucesso'.format(s))
