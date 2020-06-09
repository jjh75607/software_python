import math


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("(X, Y) = ", self.x, self.y)

    def distanceTo(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx * dx + dy * dy)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def print(self):
        print("(X, Y, Z) = ", self.x, self.y, self.z)

    def distanceTo(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        dz = self.z - point.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)


class Point4D(Point3D):
    def __init__(self, w, x, y, z):
        super().__init__(x, y, z)
        self.w = w

    def print(self):
        print("(X, Y, Z, W) = ", self.x, self.y, self.z, self.w)

    def distanceTo(self, point):
        dw = self.w - point.w
        dxyz = super().distanceTo(point)
        dxyz = dxyz * dxyz
        return math.sqrt(dxyz + dw * dw)


p3 = Point3D(10, 20, 30)
p4 = Point3D(50, 60, 70)
print(p3.__dict__)
p3.print()
print("distance = ", p3.distanceTo(p4))

p5 = Point4D(10, 20, 30, 40)
p6 = Point4D(50, 60, 70, 80)
p5.print()
print("4d distance : ", p5.distanceTo(p6))

# p1 = Point2D(10, 20)
# p2 = Point2D(10, 60)
#
# p1.print()
# p2.print()
#
# print(p1.__dict__)
# print(p2.__dict__)
#
# print("distance between p1 and p2 = ", p1.distanceTo(p2))
# print("distance between p2 and p1 = ", p2.distanceTo(p1))
#
# print(math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y)))
