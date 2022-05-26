n = int(input('Digite um numero inteiro: '))
o = int(input("""---Opções---
[1] - Converter para Binario
[2] - Converter para Octal
[3] - Converter para Hexadecimal
---Selecione uma opção:--- 
"""))
if o == 1 :
    print(bin(n)[2:])
elif o == 2 :
    print(oct(n)[2:])
elif o == 3 :
    print(hex(n)[2:])
else:
    print('Numero incorreto')
