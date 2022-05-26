tn = int(input('Primeiro Valor: ')) , int(input('Segundo Valor: ')), int(input('Terceiro Valor: ')) , int(input('Ultimo Valor: '))
print(f'Você digitou os valores: {tn}')
print(f'O valor 9 apareceu {tn.count(9)} vezes')
if tn.count(3) > 0:
    print(f'O valor 3 apareceu pela primeira vez na {tn.index(3) + 1}ª posição')
else:
    print('não possui valor 3 em nenhum lugar')
print('Valores pares: ',end='')
for par in tn:
    if par % 2 == 0:
        print(par,end=' ')
