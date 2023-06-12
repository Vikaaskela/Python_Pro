#Task 1
#Створіть абстрактний базовий клас "Фігура" і від нього успадкуйте конкретні класи, такі як "Коло", 
#"Прямокутник", "Трикутник" і т.д. Кожен клас має мати методи для обчислення площі та периметру фігури. 
#Створіть декілька об'єктів різних фігур і виведіть їх площу та периметр.

import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def area(self):
        ...
    def perimeter(self):
        ...

class Circle(Figure):
    def area(self, r):
        return 3.14 * r ** 2

    def perimeter(self, r):
        return 2 * 3.14 *r
    
class Rectangle(Figure):
    def area(self, a, b):
        return a * b

    def perimeter(self, a, b):
        return a + b + a + b

class Triangle(Figure):
    def area(self, a, h):
        return (a * h) / 2

    def perimeter(self, a, b, c):
        return a + b + c
    
x = Circle()
y = Rectangle()
z = Triangle()
print(x.area(5))
print(x.perimeter(5))
print(y.area(2, 2))
print(y.perimeter(2, 2))
print(z.area(2, 3))
print(z.perimeter(2, 3, 4))
