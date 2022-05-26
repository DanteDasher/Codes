ln = list()
while True:
    n = int(input('Digite um valor'))
    if n in ln:
        print('A lista ja possui este valor')
    else:
        ln.append(n)
    q = ''
    while True:
        q = input('Quer continuar? [S/N]').upper()
        if q == 'S':
            break
        elif q == 'N':
            break
    if q == 'N':
        break
ln.sort()
print(ln)