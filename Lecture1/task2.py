#Task 2
#Необхідно розробити Python-скрипт, який буде повертати користувачеві меню ресторану. 
#Зазвичай, меню ресторану містить наступні елементи:
#- Категорії страв (наприклад, закуски, основні страви, десерти).
#- Страви у кожній категорії.
#Основні класи, які необхідно створити для реалізації меню ресторану:
#Клас Страва: відповідає за збереження інформації про окрему страву, включаючи її назву, опис та ціну.
#Клас Категорія страв: відповідає за збереження страв, які належать до конкретної категорії. Включає список об'єктів "Страва".
#Клас Меню: відповідає за збереження всіх категорій страв та їхнього вмісту. Включає список об'єктів "Категорія страв".
#Клас Замовлення: відповідає за збереження списку страв, які замовив клієнт, та їхньої ціни.

class Dish:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} "{self.description}": {self.price:.2f}'


class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        return f'{self.name} "{self.dishes}"'

class Menu:
    def __init__(self, categories):
        self.categories = categories

    def __str__(self):
        return f'{self.categories}'

class Order:
    def __init__(self):
        self.dishes = []
        self.quantities = []

    def add_item(self, item: MenuCategory, quantity = 1):
        self.items.append(item)
        self.quantities.append(quantity)

    def remove_item(self, item, quantity = 1):
        self.items.append(item)
        self.quantities.append(quantity)

    def calculate_total(self):
        res = ''
        total = []
        for dishes, quantity in zip(self.dishes, self.quantities):
            res += f'{dishes} x {quantity} = {dishes.price * quantity} грн\n'
            total.append(dishes.price * quantity)
        return f'{res}Total: {sum(total)}'   


order = Order()
dishes_1 = Dish('potatoes', 'fried', 100)
dishes_2 = Dish('steak', 'beef', 200)
dishes_3 = Dish('beer', 'unfiltered', 80)


order.add_dishes(dishes_1)
order.add_dishes(dishes_2)
order.add_dishes(dishes_3)

print(order)