'''
from random import randint
with open('test.txt', 'w') as f:
    for i in range(1_000_000):
        if i % 9 == 0:
            f.write('Hello\n')
        else:
            f.write(f'{randint(0, 5)}\n')
'''

with open ('test.txt') as f:
    data = f.readlines()
    s = 0
    for item in data:
        if item.strip().isdigit():
            s += int(item)
    print(s)

with open ('test.txt') as f:
    s = 0
    for item in f:
        if item.strip().isdigit():
            s += int(item)
    print(s)

with open ('test.txt') as f:
    s = sum(int(item) for item in f if item.strip().isdigit())
    print(s)

import timeit

stmt_1 = """
with open('test.txt') as f:
    data = f.readlines()
    s = 0
    for item in data:
        if item.strip().isdigit():
            s += int(item)
"""

stmt_2 = """
with open('test.txt') as f:
    s = 0
    for item in f:
        if item.strip().isdigit():
            s += int(item)
"""

stmt_3 = """
with open('test.txt') as f:
    s = sum(int(item) for item in f if item.strip().isdigit())
"""

print(timeit.timeit(stmt_1, number=100))
print(timeit.timeit(stmt_2, number=100))
print(timeit.timeit(stmt_3, number=100))