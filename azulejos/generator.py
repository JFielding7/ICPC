from random import randint

n = 7
print(n)

for _ in range(n):
    print(1, end=" ")
print()

for _ in range(n):
    print(randint(100, 200), end=" ")
print()

for _ in range(n):
    print(1, end=" ")
print()

for _ in range(n):
    print(randint(1, 100), end=" ")
print()
