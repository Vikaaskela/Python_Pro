#Task 1
#Створіть клас "Рахунок", який має приватну властивість "баланс". Використайте дескриптор для реалізації
#контролю доступу до цієї властивості. Додайте властивість balance з декоратором @property, яка повертає 
#значення балансу. Визначте метод __setattr__, який забороняє безпосереднє змінення значення балансу. 
#Також визначте метод __getattr__, який повертає повідомлення про те, що властивість не існує, якщо 
#доступ до неї спробувати отримати. Використовуйте цей клас для створення об'єкту рахунку та спробуйте 
#змінити значення балансу та отримати доступ до неіснуючої властивості.

class BalanceDescriptor:

    def __init__(self, attr):
        self. __balance = 1000
        self.attr = attr

    def __set__(self, instance, value):
        instance.__dict__[self.attr] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr] +  self.__balance 

    def __delete__(self, instance):
        ...


class Score:

    def __init__(self, balance):
        self. __balance = balance
    

    @property
    def balance(self):
        return f'balance'

    def __getattr__(self, item):
        self.__dict__[item] = 'the property does not exist'
        return self.__dict__[item]

    def __setattr__(self, key, value):
        if key == 'balance':
            if not isinstance(value, int):
                raise TypeError()
            if value <= 0:
                raise ValueError()
            self.__dict__[key] = value


    balance = BalanceDescriptor('balance')


x = Score(1000)
print(x.balance)