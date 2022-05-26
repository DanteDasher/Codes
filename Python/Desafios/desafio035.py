v1 = int(input('Digite o valor do primeiro lado: '))
v2 = int(input('Digite o valor do segundo lado: '))
v3 = int(input('Digite o valor do terceiro lado: '))
if(v1 + v2 > v3 and v2 + v3 > v1 and v3 + v1 > v2):
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')