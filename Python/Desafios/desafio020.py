from random import sample
a1 = input('Digite o nome do Primeiro Aluno: ')
a2 = input('Digite o nome do Segundo Aluno: ')
a3 = input('Digite o nome do Terceiro Aluno: ')
a4 = input('Digite o nome do Quarto Aluno: ')
print('A ordem da Apresentação sera: {}'.format(sample([a1,a2,a3,a4],k=4)))