'''
a =  int(input('a='))
b =  int(input('b='))

print(f'a // b = {a // b}')
'''
'''
try:
    a =  int(input('a='))
    print(a)
except:
    print('Input error!')
'''
'''
while True:
    try:
        a =  int(input('a='))
        b =  int(input('b='))
        print(f'a // b = {a // b}')
        break
    except (ValueError, ZeroDivisionError) as error:
        print(error)
'''
'''
def add(a: int, b: int) -> int:
   if isinstance(a, int) and isinstance(b, int):
    return a + b
   
   raise ValueError('Params a or b must be int numbers.')

print(add('2', '3') + 2.5)
'''
'''
def add(a: int, b: int) -> int:
   if isinstance(a, int) and isinstance(b, int):
    return a + b
   
   raise ValueError('Params a or b must be int numbers.')

try:
    print(add('2', '3') + 2.5)
except ValueError as error:
   print(error)
'''
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

try:
    pr_1 = Product('banana', 10)
except (PriceError, TypeError) as error:
    print(error)