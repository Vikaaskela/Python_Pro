#Розштрення класу, спочатку був клас котиків і песиків, а потім додали птахів
class Animal:
    def say(self):
        ...


class Cat(Animal):
    def say(self):
        return 'May'


class Dog(Animal):
    def say(self):
        return 'Woof'


class Bird(Animal):
    def say(self):
        return 'Kar-Kar'


def communicate(animal: Animal):
    return animal.say()


def main():
    animal_type = input('type=')
    animals = {
        'cat': Cat(),
        'dog': Dog(),
        'bird': Bird()
    }

    print(communicate(animals[animal_type]))


if __name__ == '__main__':
    main()