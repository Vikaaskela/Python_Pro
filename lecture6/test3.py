'''
def gen_item(stop):
    index = 0
    while index < stop:
        index += 1
        return index
    
print(gen_item(10))
print(gen_item(10))
print(gen_item(10))
'''
'''
def gen_item(stop):
    index = 0
    while index < stop:
        index += 1
    return index
    
print(gen_item(10))
print(gen_item(10))
print(gen_item(10))
'''
'''
def gen_item(stop):
    index = 0
    while index < stop:
        yield index
        index += 1
   
for item in gen_item(10):
    print(item)
'''
'''
def fibonacci(n):
    index = 0
    prev, current = 0, 1
    while index < n:
        prev, current = current, current + prev
        yield current
        index += 1

for i in fibonacci(5):
    print(i)
'''

def fibonacci(n):
    index = 0
    prev, current = 0, 1
    while index < n:
        yield current
        prev, current = current, current + prev
        index += 1

x = (i ** 2 for i in range(20))
for item in x:
    print(item)
    #print(sum(x))
