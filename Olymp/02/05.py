n, m, c, k = map(int, input().split())

totl = n * m

need = totl - k

if need <= 0:
    print(0)
else:
    pack = (need + 199) //200
    print(pack *c)