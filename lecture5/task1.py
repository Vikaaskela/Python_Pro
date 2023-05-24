#Task 1
#Для попереднього проєкту (Замовлення продуктів в магазині) реалізувати можливість поєднання двох 
#кошиків в один за допомогою оператора "+=".
class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    
    def __iadd__(self, other: Product):
        if not isinstance(other, Product):
            return NotImplemented
        if other in self.products:
            raise ValueError()
        
        self.products.append(other)
        return self
    
    def __getitem__(self, item):
        return self.products[item]

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
pr_4 = Product('kiwi', 80)

order = Cart()
order += pr_1
order += pr_2
order += pr_3
order += pr_4


for item in order:
    print(item)


print(order)