from functools import reduce


try:
    while 1:
        print(reduce(lambda total, curr: curr + total, map(lambda col: float(col.replace(" ", "")), input().split(","))))
except EOFError:
    pass
