class PriceDescriptor:

    def __init__(self, attr):
        self.shipping_price = 0.1
        self.add_price = 0.2
        self.attr = attr

    def __set__(self, instance, value):
        instance.__dict__[self.attr] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr] + instance.__dict__[self.attr] * (self.shipping_price + self.add_price)

    def __delete__(self, instance):
        ...


class Cart:

    def __init__(self, price):
        self.price = price

    price = PriceDescriptor('price')


x = Cart(100)
print(x.price)