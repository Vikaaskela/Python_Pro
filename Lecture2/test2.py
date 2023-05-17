#множинне наслідування
class A:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f'Hello from A'
    
class B:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f'Hello from B'
    

class C(A, B):
    def __init__(self, name):
        super().__init__(name)
    

x = C('Oleh')
print(C.__mro__)
print(x.greetings())  

