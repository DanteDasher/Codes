n1 = int(input('PRIMEIRO VALOR: '))
n2 = int(input('SEGUNDO VALOR: '))
o = 0
r = 0
while o != 5:
    o = int(input('''
    OPÇÕES
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NUMEROS
    [5] - ENCERRAR
    ESCOLHA:
    '''))
    if o == 1:
        r = n1 + n2
        print('O resultado da soma é: {}'.format(r))
    elif o == 2:
        r = n1 * n2
        print('O resultado da multiplicação é: {}'.format(r))
    elif o == 3:
        if n1 > n2:
            print('O numero {} é maior que {}'.format(n1,n2))
        elif n1 < n2:
            print('O numero {} é maior que {}'.format(n2,n1))
        else:
            print('os dois numeros são iguais')
    elif o == 4:
        n1 = int(input('PRIMEIRO VALOR: '))
        n2 = int(input('SEGUNDO VALOR: '))
    elif o == 5:
        print('See you next time')
    else:
        print('Opção invalida, tente novamente')
