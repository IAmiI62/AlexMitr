n = int(input())
m = 0
d = 0

for _ in range(n):
  car= int(input())
  if car % 3 == 0:
    m += 2
  else:
    d += 1

print(f"{m}:{d}")