def has(a, *b):
    for i in b[0]:
        if a == i:
            return True
    return False


def intersect(a, b):
    s = set()
    for i in a:
        if has(i, list(b)):
            s.add(i)

    return s


a = {1, 2, 3}
b = {2, 3, 4}
print(intersect(a, b))  # {2, 3}을 출력
