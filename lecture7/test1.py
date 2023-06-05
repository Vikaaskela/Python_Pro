'''
def add(a, b):
    return a + b

print(id(add))
print(type(add))
'''
#Функцію можна повернути з іншої функції
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def calc(cmd: str):
    if cmd == '+':
        return add
    if cmd == '-':
        return sub
    if cmd == '*':
        return mul
    if cmd == '/':
        return div


a, b = int(input('a=')), int(input('b='))
cmd = input('cmd=')
print(f'Reult is {calc(cmd)(a, b)}')