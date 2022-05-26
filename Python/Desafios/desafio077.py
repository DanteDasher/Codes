tn = ('torta','biscoito','amendoim','antedeguemon','rengoku','bolacha','lamen','chapolin')
for name in tn:
    print(f'na palavra {name.upper()} temos ',end='')
    for c in range(0,len(name)):
        if name[c] == 'a' or name[c] == 'e' or name[c] == 'i' or name[c] == 'o' or name[c] == 'u':
            print(name[c],end=' ')
    print('\n')