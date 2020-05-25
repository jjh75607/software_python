score_list = [1, 8, 70, 52, 23]
for x in score_list:
    if x < 80:
        continue

    print(x)

score_list = [1, 8, 70, 52, 23]
for x in score_list:
    if x < 80:
        break

    print(x)

for letter in 'python':
    if letter == 'h':
        pass
    else:
        print(letter)

var = 32
(var > 0) if print("sad") else print("asd")

# _ ㄱㅏ장 최근 인터프린터에 변경된 값, 사용되지 않는 변수를 표현하기도 함
for _ in range(2):
    print("hi")


def sum(x, y):
    '''
    :param x:
    :param y:
    :return: x + y
    '''

    return x + y


def test(x, y=0, b=1):
    return 123


test(x=1, y=123, b=3)


def var_s(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


a = var_s(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def k(**ke):
    print(ke)


k(name="name", age=12, asd=';adsf')  # ㄱㅏ변인자 딕셔너리로


def g(name, age, addr):
    print(name)


f = ['name', 123, 'ad']
g(*f)
t = ('name', 123, 'ad')
g(*f)


def x(d):
    return d, d * d, d ** 2


e, s, q = x(1)
