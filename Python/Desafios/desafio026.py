f = input('Digite uma frase: ').strip()
print('Esta frase possui {} letras A'.format(f.lower().count('a')))
print('A primeira letra A aparece na posição: {}'.format(f.lower().find('a')))
print('A ultima letra A aparece na posição: {}'.format(f.lower().rfind('a')))