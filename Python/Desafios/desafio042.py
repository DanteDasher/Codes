a = int(input('Primeiro Lado: '))
b = int(input('Segundo Lado: '))
c = int(input('Terceiro Lado: '))
if a + b <= c or b + c <= a or a + c <= b:
    print('Não forma triangulo')
elif a == b ==c :
    print('Forma um triangulo equilatero')
elif a != b != c:
    print('Forma um triangulo escaleno')
else:
    print('Forma um triangulo Isóceles')
