def to_str(func):
    def inner(*args, **kwargs):
        return f'{func(*args, **kwargs)}'
    return inner

@to_str
def add(x, y):
    return x + y

@to_str
def mul(x, y):
    return x * y

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @to_str
    def add(self):
        return self.x + self.y


print(type(add(3, 4)))
x = A(3, 7)
print(type(x.add()))
