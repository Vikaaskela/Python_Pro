#Task 3
#Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.
def geometric(n):
    current =  2
    while  n != 0:
        current = current * 2
        yield current
        n -= 1

for i in geometric(6):
    print(i)