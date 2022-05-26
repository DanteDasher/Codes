from datetime import date
a = int(input('Ano de Nascimento: '))
i = date.today().year - a
print('Sua idade é {}'.format(i))
if i > 25:
    c = 'MASTER'
elif i > 19:
    c = 'SÊNIOR'
elif i > 14:
    c = 'JÚNIOR'
elif i > 9:
    c = 'INFANTIL'
else:
    c = 'MIRIM'
print('Sua categoria é: {}'.format(c))