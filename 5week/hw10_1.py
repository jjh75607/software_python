def has(a, *b):
    return a in b[0]


a = 5
b = [1, 2, 3, 5, 6, 7]
print(has(5, b))
