#Task 1
#Створіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, 
#ціну та опис товару. Створіть декілька інстансів класу Product.
#Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. 
#Кошик може містити декілька товарів певної кількості. Реалізуйте метод обчислення вартості кошика.
#В усіх класах має бути визначений метод str
'''
class Product:

    def __init__(self, name: str, descr: str, price: float):
        self.name = name
        self.descr = descr
        self.price = price
        

    def __str__(self):
        return f'{self.name} "{self.descr}": {self.price:.2f}'
    

class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []


    def add_product(self, product, quantity = 1):
        self.products.append(product)
        self.quantities.append(quantity)


    def __str__(self):
        res = ''
        total = []
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
            total.append(product.price * quantity)
        return f'{res}Total: {sum(total)}'   

          
        
cart = Cart()
product_1 = Product('milk', 'Bila Liniya', 45)
product_2 = Product('apple', 'Golden', 50)
product_3 = Product('bread', 'Palianytsia', 30)


cart.add_product(product_1, 3)
cart.add_product(product_2, 2)
cart.add_product(product_3)


print(cart)
'''
class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity=1):
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        result = ''
        for product, quantity in zip(self.products, self.quantities):
            result += f'{product} x {quantity} = {product.price * quantity}\n'

        return f'{result}\nTotal: {self.total()}'


pr_1 = Product('banana', 50)
pr_2 = Product('apple', 60)
pr_3 = Product('orange', 70)

order = Cart()
order.add_product(pr_1, 4)
order.add_product(pr_2)
order.add_product(pr_3)

print(order)