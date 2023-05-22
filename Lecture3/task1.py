#Task 1
#Модифікуйте перше домашнє завдання (Про замовлення), додавши перевірки в методи класів та обробку 
#виключних ситуацій.При спробі встановити від'ємну або нульову вартість товару треба викликати виняткову
#ситуацію, тип якої реалізувати самостійно.
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler('D:\VISH\Vika project\Python projects\Python Pro\Python_Pro\Lecture3\logtask1.txt')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)


class PriceError(Exception):
    def __init__(self,price, msg):
        self.price = price
        self.msg = msg

    
class Product:
    def __init__(self, title: str, price: int | float):
        if not isinstance(price, int | float):
            raise TypeError()
        if price <= 0:
            raise PriceError(price, 'Price can not be less than zero')
        self.title = title
        self.price = price

    def __str__(self):
        return self.title


class Cart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError()
        self.products.append(product)
        self.quantities.append(quantity)
        logger.info(f'Add:{product} - {quantity}')

    def remove_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError()
        if product not in self.products:
            logger.info(f'Remove error:{product}')
            raise ValueError
        
        index = self.products.index(product)
        self.quantities[index] -= quantity
        if self.quantities[index] <= 0:
            del self.products[index]
            del self.quantities[index]

        logger.info(f'Remove:{product} - {quantity}')

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        result = ''
        for product, quantity in zip(self.products, self.quantities):
            result += f'{product} x {quantity} = {product.price * quantity}\n'

        return f'{result}\nTotal: {self.total()}'


try:
    pr_1 = Product('banana', 10)
    pr_2 = Product('apple', 20)
    pr_3 = Product('orange', 30)
    pr_4 = Product('kiwi', 10)
except (PriceError, TypeError) as error:
    print(error)

order = Cart()
order.add_product(pr_1, 4)
order.add_product(pr_2)
order.add_product(pr_3)

print(order)  