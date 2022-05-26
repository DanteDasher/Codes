from random import randint
v = 0
while True:
    c = randint(0,10)
    e = input('Par ou Impar? [P/I]').upper()
    n = int(input('Digite um valor: '))
    if e == 'P':
        if (n + c) % 2 == 0:
            print(f'Você jogou {n} e o computador {c}, o total {n + c} é par \nVocê Venceu!!!')
            v += 1
        else:
            print(f'Você jogou {n} e o computador {c}, o total {n + c} é impar \nVocê Perdeu!!!')
            break
    elif e == 'I':
        if (n + c) % 2 == 0:
            print(f'Você jogou {n} e o computador {c}, o total {n + c} é par \nVocê Perdeu!!!')
            break
        else:
            print(f'Você jogou {n} e o computador {c}, o total {n + c} é impar \nVocê Venceu!!!')
            v += 1
    else:
        print('tente novamente')
print(f'GAME OVER. Você Venceu {v} Vezes')