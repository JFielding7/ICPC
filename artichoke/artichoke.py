from math import sin, cos


p, a, b, c, d, n = tuple(map(int, input().split(" ")))
max_price = -float('inf')
max_decline = 0

for i in range(1, n + 1):
    price = p * (sin(a * i + b) + cos(c * i + d) + 2)
    max_decline = max(max_decline, max_price - price)
    max_price = max(max_price, price)

print(max_decline)
