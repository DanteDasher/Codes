s = int(input('Valor do saque?' ))
cc = s // 50
s = s - (50 * cc)
cv = s // 20
s = s - (20 * cv)
cd = s // 10
s = s - (10 * cd)
cu = s // 1
print(f'''
Total de {cc} cédulas de R$:50
Total de {cv} cédulas de R$:20
Total de {cd} cédulas de R$:10
Total de {cu} cédulas de R$:1
''')
