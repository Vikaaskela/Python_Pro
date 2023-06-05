'''
def factorial():
    results = [1, 1]

    def inner(n):
        if n < len(results):
            return results[n]
        res = results[-1]
        for i in range(len(results), n + 1):
            res *= i
            results.append(res)
        return res
    return inner


f = factorial()
print(f(0))
print(f(1))
print(f(5))
print(f(7))
print(f(3))
print(f(10))
'''
'''
def decorator(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    
    return inner

def text(name):
    return f'Hello, {name}'

res = decorator(text)
print(res('Oleh'))
'''
def decorator(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    
    return inner
@decorator
def text(name):
    return f'Hello, {name}'


print(text('Oleh'))