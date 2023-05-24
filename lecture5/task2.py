#Task 2
#Для попереднього проєкту (Меню Ресторану) реалізувати можливість додавання страв з меню до замовлення 
#через оператор "+=".
class Dish:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} uah'


class Category:
    def __init__(self, title):
        self.title = title
        self.dishes = []

    #def add_dish(self, dish):
    #    self.dishes.append(dish)

    def __iadd__(self, other: Dish):
        if not isinstance(other, Dish):
            return NotImplemented
        if other in self.dishes:
            raise ValueError()
        
        self.dishes.append(other)
        return self
    
    def __getitem__(self, item):
        return self.dishes[item]

    def __str__(self):
        return f"{'*' * 10}{self.title}{'*' * 10}\n" + '\n'.join(map(str, self.dishes))


class Menu:
    def __init__(self):
        self.categories = []

    #def add_category(self, category):
    #    self.categories.append(category)

    def __iadd__(self, other: Category):
        if not isinstance(other, Category):
            return NotImplemented
        if other in self.dishes:
            raise ValueError()

        self.categories.append(other)
        return self

    def __getitem__(self, item):
        return self.categories[item]

    def __str__(self):
        return '\n'.join(map(str, self.categories))

'''
dish_1 = Dish('Страва 1', 100)
dish_2 = Dish('Страва 2', 101)
dish_3 = Dish('Страва 3', 102)
dish_4 = Dish('Страва 4', 103)
dish_5 = Dish('Страва 5', 104)
dish_6 = Dish('Страва 6', 105)
dish_7 = Dish('Страва 7', 106)
dish_8 = Dish('Страва 8', 107)
dish_9 = Dish('Страва 9', 108)
dish_10 = Dish('Страва 10', 109)

cat_1 = Category('Основні страви')
cat_1.add_dish(dish_1)
cat_1.add_dish(dish_2)
cat_1.add_dish(dish_3)
cat_1.add_dish(dish_4)
cat_1.add_dish(dish_5)

cat_2 = Category('Перші страви')
cat_2.add_dish(dish_6)
cat_2.add_dish(dish_7)
cat_2.add_dish(dish_8)
cat_2.add_dish(dish_9)
cat_2.add_dish(dish_10)

menu = Menu()
menu.add_category(cat_1)
menu.add_category(cat_2)

print(menu)
'''
class Oder:

    def __init__(self):
        self.dishes = []
        self.quantities = []


    def __iadd__(self, other: Dish):
        if not isinstance(other, Dish):
            return NotImplemented
        if other in self.dishes:
            raise ValueError()

        self.dishes.append(other)
        return self

    def __getitem__(self, item):
        return self.dishes[item]

    def total(self):
        return sum(dish.price * quantity for dish, quantity in zip(self.dishes, self.quantities))

    def __str__(self):
        result = ''
        for dish, quantity in zip(self.dishes, self.quantities):
            result += f'{dish} x {quantity} = {dish.price * quantity}\n'

        return f'{result}\nTotal: {self.total()}'


dish_1 = Dish('Страва 6', 105)
dish_2 = Dish('Страва 7', 106)
dish_3 = Dish('Страва 8', 107)
dish_4 = Dish('Страва 9', 108)

order = Oder()
order += dish_1
order += dish_2
order += dish_3
order += dish_4

order_1 = order[::2]
order_2= order[1::2]

for item in order_1:
    print(item)
print('*' * 10)
for item in order_2:
    print(item)


print(order)