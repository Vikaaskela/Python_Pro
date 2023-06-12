'''
class Student:

    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.__passport = passport

   
    def passport(self):
        return 'x' * 6


x = Student('Ivan', 'Ivanov', '12345678')
print(x.passport)
'''


class Student:

    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self. passport = passport

    @property
    def passport(self):
        return 'x' * 6

    @passport.setter
    def passport(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if len(value.strip().replace(' ', '')) < 8:
            raise ValueError()
        self.__passport = value

    @passport.deleter
    def passport(self):
        ...



x = Student('Ivan', 'Ivanov', '12345678')
print(x.passport)
x.passport = 'QQ123456'
del x.passport
print(x.passport)