#Task 1
#Створіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, 
#ціну та опис товару. Створіть декілька інстансів класу Product.
#Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. 
#Кошик може містити декілька товарів певної кількості. Реалізуйте метод обчислення вартості кошика.
#В усіх класах має бути визначений метод str
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
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
        return res
    

          

cart = Cart()
product_1 = Product('milk', 'Bila Liniya', 45)
product_2 = Product('apple', 'Golden', 50)
product_3 = Product('bread', 'Palianytsia', 30)


cart.add_product(product_1)
cart.add_product(product_2, 3)
cart.add_product(product_3, 2)


print(cart)
