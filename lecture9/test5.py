'''
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def say(self):
        ...

class Cat(Animal):
    def say(self):
        return "May"
    
x = Cat()
print(x.say())
'''

class Animal:
    
    def say(self):
        return NotImplementedError

class Cat(Animal):
    def say(self):
        return "May"
    
x = Cat()
print(x.say())