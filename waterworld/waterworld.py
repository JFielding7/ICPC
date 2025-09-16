n, m = tuple(map(int, input().split()))
total = 0

for _ in range(n):
    for num in map(int, input().split()):
        total += num

print(total / (n * m))
