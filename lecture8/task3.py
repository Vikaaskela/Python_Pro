#Task 3
#Напишіть декоратор, який перехоплює та обробляє виключення, що виникають у функції.
def handle_exceptions(func):
    def inner(*args, **kwargs):
        return ...
    return inner

@handle_exceptions
def divide(a, b):
    return a / b

divide(5, 0)
