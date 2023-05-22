#Task 1
#Рознесіть класи, які використовували під час вирішення завдання про замовлення та меню для ресторану 
#по модулям. Переконайтеся у працездатності проєктів.

from product import Product
import cart
from  try_except import pr_1, pr_2, pr_3


cart = cart.Cart()
cart.add_product(pr_1, 4)
cart.add_product(pr_2)
cart.add_product(pr_3)

if __name__ == '__main__':
    print(cart)