c = float(input('\033[0:30:47mDigite o valor da casa: R$ \033[m'))
s = float(input('Digite o valor do Salario: R$ '))
a = int(input('Em quantos anos pretende pagar a Casa? '))
if (c / (a * 12) > s * 0.3):
    print('Financiamento REPROVADO, valor da parcela: R$ {:.2f}'.format(c / (a * 12)))
else:
    print('Financiamento APROVADO, valor da parcela: R$ {:.2f}'.format(c / (a * 12)))