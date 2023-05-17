#Task 1
#Модифікуйте перше домашнє завдання (Про замовлення), додавши перевірки в методи класів та обробку 
#виключних ситуацій.При спробі встановити від'ємну або нульову вартість товару треба викликати виняткову
#ситуацію, тип якої реалізувати самостійно.
class PriceError(Exception):
    def __init__(self,price, msg):
        self.price = price
        self.msg = msg

    def __str__(self):
        return f'Value = {self.price}\n{self.msg}'

class Product:

    def __init__(self, title: str, price: int | float):
        if not isinstance(price, int | float):
            raise TypeError()
        if price <= 0:
            raise PriceError(price, 'Price can not be less than zero')
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'
    
try:
    pr_1 = Product('banana', 10)
except (PriceError, TypeError) as error:
    print(error)


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