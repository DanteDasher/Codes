ln = list()
ln.append(int(input('Digite um numero')))
for c in range(0,4):
    t = int(input('Digite um numero'))
    if t > ln[-1]:
        ln.append(t)
    elif t < ln[0]:
        ln.insert(0,t)
    else:
        for ca in range(0,c):
            if t > ln[ca] and t < ln[ca+1]:
                ln.insert(ca+1,t)
print(ln)