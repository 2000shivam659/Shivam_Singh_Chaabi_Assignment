# Looking at the below code, print down the final values of A0, A1, ...An
from functools import reduce


A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(A0)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
print(A1)  # range(0, 10)

A2 = sorted([i for i in A1 if i in A0])
print(A2)  # []

A3 = sorted([A0[s] for s in A0])
print(A3)  # [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
print(A4)  # [1, 2, 3, 4, 5]

A5 = {i: i * i for i in A1}
print(A5)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i, i * i] for i in A1]
print(A6)  # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
print(A7)  # 21

A8 = map(lambda x: x * 2, [1, 2, 3, 4])
print(A8)  # <map object at 0x000002BA481ABDC0>

A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])
print(A9)  # <filter object at 0x000002728C6ABE20>
