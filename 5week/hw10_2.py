def has(a, *b):
    return a in b[0]


def intersect(a, b):
    s = set()
    for i in a:
        if has(i, list(b)):
            s.add(i)

    return s



a = {1, 2, 3}
b = {2, 3, 4}
print(intersect(a, b))  # {2, 3}을 출력
