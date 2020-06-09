import math
import gc


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("x, y : ", self.x, self.y)

    def distanceTo(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx * dx + dy * dy)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def print(self):
        print("x, y,z : ", self.x, self.y, self.z)

    def distanceTo(self, point):
        dz = self.z - point.z
        dxy = super().distanceTo(point)
        dxy = dxy * dxy
        return math.sqrt(dxy + dz * dz)


p1 = Point2D(10, 20)
p1.z = "인스턴스 변수 추가 방법 1"  # Point2D에만 추
p2 = Point2D(20, 30)

p1.print()
p2.print()

print(p1.__dict__)  # 현재 인스턴스 안의 변수 목록
print(p1.distanceTo(p2))

gc.collect() # 가비지 컬렉터