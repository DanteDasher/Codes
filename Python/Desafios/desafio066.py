c = t = 0
while True:
    n = int(input('Digite um numero[999 para parar]: '))
    if n == 999:
        break
    c += 1
    t += n
print(f'A soma dos {c} valor é {t}')
