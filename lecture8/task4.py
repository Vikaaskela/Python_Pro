#Task 4
#Напишіть декоратор, який вимірює час виконання функції.

import time

def measure_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("Time: {}s.".format(round(end-start, 5)))
        return res
    return wrap

@measure_time
def some_function(x):
    time.sleep(2)
    return x * x * x

print(some_function(3))
