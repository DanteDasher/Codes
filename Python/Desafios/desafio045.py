from random import randint
c = randint(1,3)
p = int(input('''Opções
[1] - Pedra
[2] - Papel
[3] - Tesoura
Escolha: '''))
if p == c:
    print('Empate!')
elif p == 1 and c == 3:
    print('Ganhou!!! Pedra Quebra Tesoura')
elif p == 1 and c == 2:
    print('Perdeu!!! Papel Embrulha Pedra')
elif p == 2 and c == 1:
    print('Ganhou!!! Papel Embrulha Pedra')
elif p == 2 and c == 3:
    print('Perdeu!!! Tesoura Corta Papel')
elif p == 3 and c == 2:
    print('Ganhou!!! Tesoura Corta Papel')
elif p == 3 and c == 1:
    print('Perdeu!!! Pedra Quebra Tesoura')
else:
    print('Opção invalida')
