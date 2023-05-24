#Task 2
#Модифікуйте друге домашнє завдання (Дисконт),  додавши перевірки в методи класів та обробку виключних 
#ситуацій.При спробі встановити знижку не в межах 0-100 % треба викликати виняткову ситуацію, тип якої 
#реалізувати самостійно.
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler('./Lecture3/logtask2.txt')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

class RateError(Exception):
    def __init__(self,rate, msg):
        self.rate = rate
        self.msg = msg

    def __str__(self):
        return f'Value = {self.rate}\n{self.msg}'

class Discount:
    def __init__(self, rate: float = 0):
        if not isinstance(rate, int | float):
            raise TypeError()
        if not 0 <= rate <= 1:
            raise RateError(rate, 'Rate can not be less than zero or more than 1')

        self.__rate = rate
      
    def discount(self):
        return self.__rate


class RegularDiscount(Discount):
    def __init__(self, rate=0.1):
        super().__init__(rate)


class SilverDiscount(Discount):
    def __init__(self, rate=0.2):
        super().__init__(rate)


class GoldDiscount(Discount):
    def __init__(self, rate=0.3):
        super().__init__(rate)


class Product:

    def __init__(self, name: str, price: float):
        if not isinstance(price, int | float):
            raise TypeError()
        if price <= 0:
            raise ValueError()
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity=1):
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
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
        return res


class Client:
    def __init__(self, name: str, discount: Discount):
        if not isinstance(discount, Discount):
            raise TypeError()
        
        self.name = name
        self.discount = discount

    def get_total_price(self, order: Cart):
        return order.total() * (1 - self.discount.discount())


    

try:
    cart = Cart()
    pr_1 = Product('banana', 10)
    pr_2 = Product('apple', 20)
    pr_3 = Product('orange', 30)
except (RateError, TypeError) as error:
    print(error)

cart.add_product(pr_1)
cart.add_product(pr_2, 3)
cart.add_product(pr_3, 2)

client = Client('User 1', GoldDiscount())
print(client.get_total_price(cart))