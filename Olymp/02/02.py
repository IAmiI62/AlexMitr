n = input().strip()

m = len(n)//2

f = int(n[:m])
s = int(n[m:])

print(s+f)