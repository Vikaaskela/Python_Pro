'''
class A:

    def greetings(self):
        return f'Hello from class {type(self).__name__}'
    
class B(A):

    ...

print(B.__dict__)
print(B.__mro__)

#x = B()
#y = A()
#print(x.greetings())  
#print(y.greetings())   
'''
'''
class A:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f'Hello {self.name}'
    
class B(A):
    def __init__(self, name):
        super().__init__(name)

    def greetings(self):
        return 'Hello from B'
    
#y = A('Oleh')
#print(y.greetings())


x = B('Oleh')
print(x.greetings())  
'''
#розширення
class A:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f'Hello {self.name}'
    
class B(A):
    def __init__(self, name):
        super().__init__(name)

    def greetings(self):
        return super().greetings() + '\Have a nice day!'
    

x = B('Oleh')
print(x.greetings())  

