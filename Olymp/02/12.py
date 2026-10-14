n = list(map(int, input().split()))

res = []

for num in n:
    for i in range(2, num + 1):
        if num % i == 0:
            res.append(i)
            break  

print(*(res))
