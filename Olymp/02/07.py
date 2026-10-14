n, t = input().split()
n = int(n)
t = float(t)

bpm = n * 60 / t

res = int(-(-bpm // 1))

print(res)
