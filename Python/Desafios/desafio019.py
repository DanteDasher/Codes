from random import choice
a1 = input('Digite o nome do Primeiro Aluno: ')
a2 = input('Digite o nome do Segundo Aluno: ')
a3 = input('Digite o nome do Terceiro Aluno: ')
a4 = input('Digite o nome do Quarto Aluno: ')
print('O Aluno escolhido para limpar o quadro foi: {}'.format(choice([a1,a2,a3,a4])))