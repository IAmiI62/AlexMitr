words = input().split()
res = []  

for word in words:
    revers = word[::-1]  # Переворачиваем слово
    res.append(revers)  # Добавляем его в result

# Выводим из списка result через пробел
print(" ".join(res))
