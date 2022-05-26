m = 0
h = 'Nenhum'
hv = 0
mn = 0
for c in range(0,4):
    n = input('NOME: ')
    i = int(input('IDADE: '))
    s = int(input('[1] - Homem  \n[outro numero] - Mulher'))
    m = m + i
    if s == 1:
        if i > hv:
            hv = i
            h = h.replace(h,n)
    else:
        if i < 20:
            mn = mn + 1
print('''
Média de Idade :{}
Homem mais Velho :{}
Mulheres com menos de 20:{}
'''.format(m/4,h,mn))