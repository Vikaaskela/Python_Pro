'''
class Average:
    def __init__(self):
        self.__numbers = []

    def __str__(self):
        ...

    def __call__(self, *args, **kwargs):
        number = args[0]
        self.__numbers.append(number)
        return sum(self.__numbers) / len(self.__numbers)


x = Average()
print(x(1))
print(x(2))
print(x(3))
'''
class Exp_2:
    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs) ** 2

@Exp_2
def add(a, b):
    return a + b

print(add(2, 2))