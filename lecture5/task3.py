#Task 3 - Додатково
#Створіть клас "Правильна Дріб" і реалізуйте методи порівняння, додавання, віднімання та множення 
#для екземплярів цього класу.
class Retional:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eq(self, other):
        return self.x * other.y == self.y * other.x
    
    def lt(self, other):
        return self.x * other.y < self.y * other.x

    def add(self, other):
        new_x = self.x * other.y + self.y * other.x
        new_y = self.y * other.y
        return Retional(new_x, new_y)

    def sub(self, other):
        new_x = self.x * other.y - self.y * other.x
        new_y = self.y * other.y
        return Retional(new_x, new_y)
    
    def mul(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Retional(new_x, new_y)
    
    def __truediv__(self, other: int):
        new_x = self.x * other.x
        new_y = other.y * self.y
        return Retional(new_x, new_y)
    
    def __str__(self):
        return f'{self.x} / {self.y}'


fraction_1 = Retional(1,2)
fraction_2 = Retional(3,4)


print(new_x, new_y)
