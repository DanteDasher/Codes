d = int(input('Digite a distancia da viagem: '))
if(d > 200):
    print('O valor da passagem é: R$ {}'.format(d*0.45))
else:
    print('O valor da passagem é: R$ {}'.format(d*0.5))