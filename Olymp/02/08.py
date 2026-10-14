x, y = map(float, input().split())

left = int(x)
if left < x:
    left += 1

right = int(y)
if right > y:
    right -= 1

if left <= right:
    ans = right - left + 1
else:
    ans = 0

print(ans)
