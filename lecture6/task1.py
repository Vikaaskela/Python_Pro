#Task 1
#Попередній проєкт (Замовлення продуктів в магазині) доповнити можливістю підтримки ітераційного протоколу.
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler(f'log.txt')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)


class PriceError(Exception):
    def __init__(self, price, msg):
        self.price = price
        self.msg = msg


class Product:
    def __init__(self, title: str, price: float | int):
        if not isinstance(price, int | float):
            raise TypeError()
        if price <= 0:
            raise PriceError(price, 'Price must be gt zero!')

        self.title = title
        self.price = price

    def __str__(self):
        return self.title

class Iterator:
    def __init__(self, items, quantities):
        self.items = items
        self.quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            self.index += 1
            return self.items[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration()


class Cart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def total(self):
        return sum(product.price * quantity for product, quantity in self)

    def __iter__(self):
        return Iterator(self.products, self.quantities)

    def add_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError()
        self.products.append(product)
        self.quantities.append(quantity)
        logger.info(f'Add: {product} - {quantity} ')

    def remove_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError()
        if product not in self.products:
            logger.error(f'Remove error: {product}')
            raise ValueError()

        index = self.products.index(product)
        self.quantities[index] -= quantity
        if self.quantities[index] <= 0:
            del self.products[index]
            del self.quantities[index]

        logger.info(f'Remove: {product} - {quantity} ')

    def __iadd__(self, other):
        self.products += other.products
        self.quantities += other.quantities
        return self

    def __str__(self):
        res = ''
        for product, quantity in self:
            res += f"{product.title} x {quantity} = {product.price * quantity} uah\n"

        return res


if __name__ == '__main__':
    try:
        pr_1 = Product('banana', 10)
        pr_2 = Product('apple', 20)
        pr_3 = Product('orange', 30)
        pr_4 = Product('kiwi', 10)

        cart_1 = Cart()
        cart_1.add_product(pr_1)
        cart_1.add_product(pr_2)

        cart_2 = Cart()
        cart_2.add_product(pr_3)
        cart_2.add_product(pr_4, 2)


        cart_1 += cart_2

        for item, quantity in cart_1:
            print(item, quantity)

    except (TypeError, PriceError) as error:
        print(error)