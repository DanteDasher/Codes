t = pc = pb = 0
while True:
    np = input('NOME: ')
    vp = int(input('PREÇO: '))
    t += vp
    if vp > 1000:
        pc += 1
    if pb == 0:
        npb = np
    elif vp < pb:
        npb = np
    f = input('Quer continuar? [S/N]').upper()
    if f == 'N':
        break
    elif f != 'S':
        while f != 'S' and f != 'N':
            print('Tente novamente')
            f = input('Quer continuar? [S/N]').upper()
        if f == 'N':
            break
print(f'VALOR TOTAL R$:{t:.2f} \nCUSTAM MAIS DE R$:1000 :{pc} \nPRODUTO MAIS BARATO: {npb}')