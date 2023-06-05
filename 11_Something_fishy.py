# Find output of following:

def f(x, l = []):
    for i in range(x):
        l.append(i * i)
    print(l)


f(2)  # [0, 1]

f(3, [3, 2, 1])  # [3, 2, 1, 0, 1, 4]

f(3)  # [0, 1, 0, 1, 4]
