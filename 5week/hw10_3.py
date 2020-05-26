def has(a, *b):
    """
    매개변수 a, list형태의 b를 받아 a가 b에 속해있는지 확인 후 True or False 반환한다.
    """
    return a in b[0]


def intersect(a, b):
    """
    위의 has 메소드를 사용하여 교집합을 구한다.
    """
    s = set()
    for i in a:
        if has(i, list(b)):
            s.add(i)

    return s


# has 사용예시
n1 = int(input("숫자를 입력 :  "))
n2 = [1, 2, 3, 4, 5]
print("has : {}".format(has(n1, n2)))

# intersect 사용예시
s1 = {3, 4, 5}
s2 = {1, 2, 3, 4, 5}
print("intersect : {}".format(intersect(s1, s2)))
