class Cat:

    def say(self):
        return 'May'


class Dog:

    def say(self):
        return 'Woof'


class Bird:

    def say(self):
        return 'Kar-Kar'

class Fish:

    def swim(self):
        return 'I can swim'

def greetings(obj):
    return f'Hello, I can speek: {obj.say()}'

x = Cat()
y = Dog()
z = Bird()
d = Fish()

print(greetings(x))
print(greetings(y))
print(greetings(z))
print(greetings(d))