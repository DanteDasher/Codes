from datetime import date
a = int(input('Ano de Nascimento: '))
d = date.today().year
i = d - a
print('Quem nasceu em {} tem {} anos em {}'.format(a, i, d))
if i == 18 :
    print('Esta na hora de se alistar')
elif i < 18 :
    print('Ainda faltam {} anos para precisar se alistar \nO alistamento sera em {}'.format(18 - i, d + (18 - i)))
else:
    print('Você ja deveria ter se alistado em {} \nSeu alistamento foi em {}'.format(i - 18, d - (i - 18)))