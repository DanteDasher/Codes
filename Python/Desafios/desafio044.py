v = float(input('Valor do Produto: '))
o = int(input('''FORMAS DE PAGAMENTO
[1] - Dinheiro/Cheque
[2] - Cartão
'''))
if o == 1:
    print('O valor total a pagar é R$:{:.2f}'.format(v * 0.9))
elif o == 2:
    o = int(input('QUANTAS PARCELAS'))
    if o == 0:
        print('Opção invalida')
    elif o == 1:
        print('O valor total a pagar é R$:{:.2f}'.format(v * 0.95))
    elif o == 2:
        print('O valor total a pagar é R$:{:.2f}'.format(v))
    else:
        print('O valor total a pagar é R$:{:.2f} em {} parcelas de R$:{:.2f}'.format(v * 1.2 , o , v * 1.2 / o))
else:
    print('Opção invalida')
