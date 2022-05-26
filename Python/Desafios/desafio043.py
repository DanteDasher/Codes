a = float(input('Altura(m)'))
p = float(input('Peso(Kg)'))
i = p / a**2
print('Seu IMC é: {:.1f} seu estado é de: '.format(i), end='')
if i > 40:
    print('Obesidade Morbida')
elif i > 30:
    print('Obesidade')
elif i > 25:
    print('SobrePeso')
elif i < 18.5:
    print('Abaixo do Peso')
else:
    print('Peso Ideal')
