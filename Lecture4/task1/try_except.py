import product
from price_error  import PriceError
try:
    pr_1 = product.Product('banana', 10)
    pr_2 = product.Product('apple', 20)
    pr_3 = product.Product('orange', 30)
    pr_4 = product.Product('kiwi', 10)
except (PriceError, TypeError) as error:
    print(error)

