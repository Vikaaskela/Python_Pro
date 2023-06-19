#Task 4
#Реалізуйте свій аналог генераторної функції range().
'''
def gen_range(a):
    index = 0
    while index < a:
        yield index
        index += 1
    
for item in gen_range(5):
    print(item)
'''
def my_range(*args):
    for item in args:
        if not isinstance(item, int):
            raise TypeError()

    start, stop, step = 0, None, 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError()

    if step == 0:
        ValueError()

    if step >= 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


for i in my_range(20, 10, -1):
    print(i)