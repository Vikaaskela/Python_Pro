class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        self.__dict__[item] = 'unknown'
        return self.__dict__[item]

    def __setattr__(self, key, value):
        if key == 'age':
            if not isinstance(value, int):
                raise TypeError()
            if value <= 0:
                raise ValueError()
            self.__dict__[key] = value

    def __str__(self):
        return f'{self.name}: {self.age}'


x = Cat('Tom', 3)
x.name = 'Jack'
x.breed = 'scotish'
print(x.breed)

print(x)