n = input('Digite Seu Nome Completo: ').strip()
print('Nome Maiúsculo: {}'.format(n.upper()))
print('Nome Minusculo: {}'.format(n.lower()))
print('Total de Letras Sem Espaços: {}'.format(len(n) - n.count(' ')))
s = n.split()
print('Total de letras do primero nome: {}'.format(len(s[0])))
#print('Total de letras do primero nome: {}'.format(n.find(' '))) "só vai funcionar com string stripada"