#Task 1
#Напишіть декоратор, який виконує певну дію перед і після виконанням функції.

def decorator_function(func):
    def inner(*args, **kwargs):
        print('Start func')
        func(*args, **kwargs)
        print('End func')
    return inner

@decorator_function
def sum(x, y):
    print (x + y)

sum(1, 2)


