def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        func()
        print('Выходим из обёртки')
    return wrapper
@decorator_function
def hello_world():
        print('Hello world!')

hello_world()
