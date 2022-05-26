while True:
    n = int(input('Quer a tabuada de qual número? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
