print(3 // 4)
print(2 ** 3)


n1 = 0o111  # 8
oct(213) # 8변환

n2 = 0xABC  # 16
hex(123) # 16변환

n3 = 0b111  # 2
bin(312) # 2진수변

str(1)
float(2)  # 실수로 변환 inf, -inf 무한대
# float(NaN)은 Not a Number 표시

# 복소수는 허수부에 j부착 complex()로 복소수 표현

abs(2)  # 절대값

print('a')
print("b")
print("""줄바꿈 가능""")
print('''줄바꿈 가능''')
# 문자열 표현

h = "h"
i = 'i'
print(h + i)
print(h * 3)

a = 'Life is too short. You need to learn python'
print(a[3]) # e
print(a[-1]) # n
print(a[4:10]) # 4 ~ 9, is to

m = 4
d = 20
print('month = '), m
print('day = '), d