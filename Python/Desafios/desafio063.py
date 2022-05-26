t = int(input('quantos termos voce quer morstrar? '))
c = 0
s = 0
a = 0
r = 0
while c != t :
    if c == 0:
        s += 1
    else:
        r = a + s
    a = s
    s = r
    print(r, '- ', end='')
    c += 1
print('FIM')