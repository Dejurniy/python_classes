class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sorted(self):
        return sorted((self.a, self.b, self.c))

    def __eq__(self, other):
        first = self.sorted()
        second = other.sorted()

        for i in range(3):
            if first[i] != second[i]:
                return False
        return True

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


triangle1 = Triangle(4, 5, 6)
triangle2 = Triangle(4, 6, 5)

print(Triangle.__eq__(triangle1, triangle2))
print(Triangle.perimeter(triangle1))
print(Triangle.area(triangle1))


class Rectangular:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sort(self):
        return sorted((self.a, self.b))

    def __eq__(self, other):
        first = self.sort()
        second = other.sort()

        for i in range(2):
            if first[i] != second[i]:
                return False
        return True

    def __gt__(self, other):
        first = self.sort()
        second = other.sort()

        for i in range(2):
            if first[i] < second[i]:
                return False
        return True


rect1 = Rectangular(10, 6)
rect2 = Rectangular(5, 10)
print(Rectangular.__eq__(rect1, rect2))
print(Rectangular.__gt__(rect1, rect2))
