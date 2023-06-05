#Task 7
#Реалізуйте генераторну функцію, яка повертатиме елементи послідовності чисел Фібоначчі.
def fibonacci(n):
    index = 0
    current, next = 0, 1
    while True:
        if index == n:
            return
        index += 1
        number = current
        current, next = next, current + next
        yield number

for i in fibonacci(10):
    print(i)
'''
def fibonacci(n):
    prev, curr = 0, 1
    index = 0
    while index < n:
        yield curr
        prev, curr = curr, prev + curr
        index += 1


for i in fibonacci(20):
    print(i)
'''