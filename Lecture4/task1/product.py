from price_error  import PriceError
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