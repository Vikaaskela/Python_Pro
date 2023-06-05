#Task 3
#Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.
'''
def geometric(n):
    current =  2
    while  n != 0:
        current = current * 2
        yield current
        n -= 1

for i in geometric(6):
    print(i)
'''
'''
нескінченна послідовність
def geom_sequence(start, stop, q):

    while True:
        yield start
        start *= q


for item in geom_sequence(2, 2):
    print(item)
'''

def geom_sequence(start, stop, q):

    while start < stop:
        yield start
        start *= q


for item in geom_sequence(2, 1025, 2):
    print(item)