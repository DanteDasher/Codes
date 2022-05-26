s = float(input('Digite o valor do salario: '))
if(s>1250):
    s = s + s * 0.1
else:
    s = s + s * 0.15
print('Seu novo salario é: R$ {:.2f}'.format(s))