tp = ('Batman',35,'Sandman',218,'Homem Aranha',20,'Horimya',8)
for c in range(0,len(tp),2):
    p = '.' * (30 - len(tp[c]))
    if tp[c+1] >= 100:
        s = ''
    elif tp[c+1] >= 10:
        s = ' '
    else:
        s = '  '
    print(f'{tp[c]}{p}R$:{s}{tp[c + 1]:.2f}')