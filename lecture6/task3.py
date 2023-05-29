#Task 3
#Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.
def geometric(n):
    index = 1
    prev, current = 1, 2
    while index < n:
        prev, current = current, current * prev
        yield current
        index += 1

for i in geometric(6):
    print(i)