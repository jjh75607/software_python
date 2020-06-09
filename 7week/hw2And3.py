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


class Triangle():
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def print(self):
        print("x1, y1 : ", self.p1.x, self.p1.y)
        print("x2, y2 : ", self.p2.x, self.p2.y)
        print("x3, y3 : ", self.p3.x, self.p3.y)

    def area(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        return 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x3 * y2 + x2 * y1))


class Rectangle(Triangle):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3)
        self.p4 = p4

        self.t1 = Triangle(self.p1, self.p2, self.p3)
        self.t2 = Triangle(self.p2, self.p3, self.p4)

    def print(self):
        super().print()
        print("x4, y4 : ", self.p4.x, self.p4.y)

    def area(self):
        return self.t1.area() + self.t2.area()


# Hw2
print("-------Hw2--------")
tri = Triangle(Point2D(15, 30), Point2D(25, 45), Point2D(30, 30))
tri.print()
print("Area of triangle : ", tri.area(), end='\n')

# Hw3
print("-------Hw3--------")
rec = Rectangle(Point2D(15, 25), Point2D(35, 45), Point2D(30, 30), Point2D(25, 35))
rec.print()
print("Area of rectangle : ", rec.area())
