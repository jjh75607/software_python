def has(a, *b):
    for i in b[0]:
        if a == i:
            return True
    return False


a = 5
b = [1, 2, 3, 5, 6, 7]
print(has(5, b))
