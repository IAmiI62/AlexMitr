price = float(input())
n = round(price * 100)

rub = n // 100
kop = n % 100

print(f"{rub} rub {kop} kop")
