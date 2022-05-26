h = mn = m = 0
while True:
    i = int(input('Digite a idade: '))
    while True:
        s = input('Sexo[M/F]: ').upper()
        if s == 'F' or s == 'M':
            break
    if i >= 18:
        m += 1
    if s == 'M':
        h += 1
    elif s == 'F' and i < 20:
        mn += 1
    f = input('Quer continuar? [S/N]').upper()
    if f == 'N':
        break
    elif f != 'S':
        while f != 'S' and f!= 'N':
            print('Tente novamente')
            f = input('Quer continuar? [S/N]').upper()
        if f == 'N':
            break
print(f'Homens: {h} \nMaiores: {m} \nMulhes com menos de 20: {mn}')