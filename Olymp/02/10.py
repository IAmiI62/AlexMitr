s = input()
revers = s[::-1]

res = ""

for char in revers:
    if char == '(':
        res += ')'
    else:
        res += '('

print(res)
