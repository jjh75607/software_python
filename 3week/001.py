import os
import sys

x = True  # 1
y = False  # 0

print(x and y)
print(x or y)
print(not x)

# ==, !=, <=, >=등

x = [1, 2, 3]
print(x in 2)

a = [1, 2, 3]
b = a
print(a is b)  # 객체 비교, 같은 메모

bytes('\x61')  # 바이트, 16진수  a

e = [0, 200, 50, 25, 10, 255]
bytearray(e)  # bytearray(b'\x00\xc82\x19\n\xff')

a = input()
print(1, 2, 3, sep='/', end='\n', file=sys.dout, flush=False)

print('%05d, %08.2f' % (168, 45.073))
print("asdasd {1} = 2, sdfsadf{0} = 1", format(1, 2))
n1 = 1
n2 = 2
"{n1}, {n2}".format(n1=n1, n2=n2)

os.getcwd()  # 현재 작업 디렉터리
os.chdir()  # 인자로 받는 디렉터리로 이동

#
os.rename()
os.remove()

# 디렉터리 생성 삭제
os.mkdir("파일이름및 경")
os.rmdir("위와동일")

os.listdir()  # 현재 경로에 존재하는 모든 디렉터리

f = open("file", 'rb')
f.close()

import pickle

f = open("x.bin", 'wb')
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)

pickle.dump(a, f)
pickle.dump(b, f)

f.close()
