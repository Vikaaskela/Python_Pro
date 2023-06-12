class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            if item == 'breed':
                self.__dict__[item] = None
                return self.__dict__[item]
            else:
                raise TypeError()


    def __setattr__(self, key, value):
        if key == 'age':
            if not isinstance(value, int):
                raise TypeError()
            if value <= 0:
                raise ValueError()
            self.__dict__[key] = value
        elif key == 'name':
            self.__dict__[key] = value

    def __delattr__(self, item):
        ...

    def __str__(self):
        return f'{self.name}: {self.age}'


x = Cat('Tom', 3)
x.name = 'Jack'
x.breed = 'scotish'
print(x.breed)

print(x)