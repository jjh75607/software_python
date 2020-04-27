str = "python is fun."
str.count('n')  # 2

str = "python is fun. programming is fun, too"

str.count('i')  # 2

str.find('fun')  # 10
str.find('xzy')  # -1
str.find('is', str.find('is') + 1)

str.index('xzy')  # error

'+-+'.join('abc')  # a+-+b+-+c

str.upper()  # 대문자변경
str.lower()  # 소문자 변경

"  abc".lstrip()
"abc  ".rstrip()
"  abc  ".strip()

"d f ff".replace(" ", '.')  # 공백을 .으로 변경

"soon jae Jung".split(' ')  # ['soon', 'jae', 'jung'] 인자를 기준으로 리스트로 자름

# 파이썬 문자열은 수정불가 객체
a = 'pithon'
b = a[:1] + 'y' + a[2:]
a.replace('i', 'y')  # 리스트 a의 값은 바뀌지 않음, 새로운 문자열 객체가 리턴

a = []  # 빈 리스트
b = [1, 2, 3]
c = [1, 2, ['a', 'b']]
print(b * 3)  # b리스트 3번 출력

print(3 in b)  # True
print(6 in b)  # False

b.append(5)  # b = [1, 2, 3, 5]
b.sort()  # 정렬
b.reverse()  # 뒤집기
b.insert(0, 3)  # 0번째 자리에 3 삽입
b.remove(100)  # 삭제

b = [1, 2, 3, 4, 5]
b.pop(1)  # 꺼낸 값 리턴 후 삭제

# b.extend([1, 2]) == b = b + [1. 2] 같음

del b[1]  # 삭제

t = (1, 2, 3)  # 튜플, 갑 변경 불가능 그거 외에는 리스트와 거의 흡사하게 사용가능

s1 = {2, 31}  # 집합, 순서가 중요하지 않고, 색인 지원하지 않고, 원소가 유니크해야한다.
s2 = {1, 7}
print(s1 & s2)  # 교집합
print(s1.intersection(s2))  # 교집합

print(s1 | s2)  # 합집합
print(s1.union(s2))

print(s1 - s2)  # 차집합
print(s1.difference(s2))

s1.add(1)  # 값 추가
s1.remove(1)  # 값 삭제

dic = {
    'name': 'gasd',
    'age': 231
}
print(dic['name'])  # gasd

dic['id'] = "id"  # 추가
del dic['id']  # 삭제
# key 값은 중복될수 없다, 중복돤더묜 가장 최근, 딕셔너리의 key값은 상수를사용(튜플, 문자열 등)

print(len(dic))
dic.clear() # 비우기
d2 = dic.copy()
d2 = dict.fromkeys(('name', 'addres'), 0) # 딕셔너리 초기화
d2.keys() # key 전체 알아내기
d2.values() # value 알아내기

list()
tuple()
dict()
set()

