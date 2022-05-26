v = int(input('Digite a velocidade do carro: '))
if(v>80):
    print('MULTADO!, o valor da multa é: R$ {:.2f}'.format((v-80)*7))