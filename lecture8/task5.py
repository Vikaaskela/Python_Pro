#Task 5
#Напишіть декоратор, який логує аргументи та результати функції.

def log_arguments_results(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " виконана ")
        return func(*args, **kwargs)
    return with_logging
   

@log_arguments_results
def add_numbers(a, b):
    return a + b

add_numbers(3, 4)