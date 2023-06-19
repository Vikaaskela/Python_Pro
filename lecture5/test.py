class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __ne__(self, other):
        return self.volume() != other.volume()

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


# import random as rnd
#
#
# boxes = [Box(rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(1, 10)) for _ in range(10)]
# for box in boxes:
#     print(box)


# boxes.sort()
# print('*' * 10)
# for box in boxes:
#     print(box)
# print(max(boxes))
# print(min(boxes))


box_1 = Box(1, 2, 3)
box_2 = Box(3, 2, 2)

print(box_1 > box_2)
'''
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __mul__(self, other: int):
         return Box(self.x * other, self.y * other, self.z * other)


    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


box = Box(1, 2, 3)
new_box = box * 3
print(box)
print(new_box)
'''

class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __mul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        if other <= 0:
            raise ValueError()
        return Box(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        if other <= 0:
            raise ValueError()
        return Box(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: int):
        if not isinstance(other, int):
            return NotImplemented
        if other <= 0:
            raise ValueError()
        self.x *= other
        self.y *= other
        self.z *= other
        return self


    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


box = Box(1, 2, 3)
print(id(box))
box *= 3

print(box)
print(id(box))
