n, m,k = map(int, input().split())
totl = n * m

box = (totl + k - 1)//k
print(box)