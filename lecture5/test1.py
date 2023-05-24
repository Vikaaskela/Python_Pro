class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


    def __gt__(self, other):
        return self.r > other.r

    def __lt__(self, other):
        return self.r < other.r

    def __ge__(self, other):
        return self.r >= other.r

    def __le__(self, other):
        return self.r <= other.r

    def __eq__(self, other):
        return self.r == other.r

    def __ne__(self, other):
        return self.r != other.r

    def __str__(self):
        return f'{self.x}, {self.y}, R={self.r}'




x = Circle(0, 0, 5)
y = Circle(1, 2, 6)

print(x < y)