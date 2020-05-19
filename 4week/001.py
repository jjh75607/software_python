# 변수 네이밍
a = b = c = 1
print(a)  # 1

x, y = 'a', 'b'
print(x, y)  # a b

del a  # delete a

total = 1 + \
        2 + \
        3  # 여러줄에 입력할

'''
    여러줄 주석
    리터럴(상수) : 값 그자체 불변
    b'\~~~' 바이트 문자열 리터럴
    u'\~~~' 유니코드 문자열 리터
'''

'''
    들여쓰기 스페이스4개로
    한 줄에 79자까지
    함수, 클래스, 큰 코드 등에는 빈줄을 넣어구분
    ㅈ주석은 별도의 줄로
    주석을 넣어
    각 연산자 사이에 빈칸을 넣고, 콤마 뒤에는 스페이스를 넣는다.
    메소드의 첫 인자는 self
    인코딩은 utf-8
    아스키 이외의 문자 식별자 x
'''

score = 80
if (score > 70):
    print("Good score")
elif (score > 60):
    print("Bad score")
else:
    print("b")

sum = 0
i = 1
while (x <= 100):
    sum += x
    x += 1

print(sum)

i = int(input())
t = 1
r = 1

while (t < i):
    r *= t
    t += 1

print("fac {},{}".format(t, r))

scoreList = [70, 20, 35, 60]
for i in scoreList:
    print(i)

dict = {'name': "abc", "age": 123}
for key, value in dict.items():
    print(key, value)

list(range(1, 101))  # 1 ~ 100

r = range(1, 11, 2)



