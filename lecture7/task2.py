#Task 2
#Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - 
#https://en.wikipedia.org/wiki/Memoization .Використовуйте отриманий механізм для прискорення функції 
#рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.
'''
def fibonacci():
    res = [1, 1]

    def next(index):
        if index < len(res):
            return res[index]
        a_0, a_1 = res[-2], res[-1]
        res.append(a_0 + a_1)
        return res[-1]
    return next


f = fibonacci()
for i in range(10):
    print(f(i))
'''
#Через замикання
def fibonacci():
    res = [1, 1]

    def next(index):
        if index < len(res):
            return res[index]
        a_0, a_1 = res[-2], res[-1]
        res.append(a_0 + a_1)
        return res[-1]
    return next

#Через ітераційний процес
def my_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        prev, curr = 1, 1
        index = 0
        while index < n:
            prev, curr = curr, prev + curr
            index += 1
        return prev


f = fibonacci()
for i in range(10):
    print(f(i))

for i in range(10):
    print(my_fibonacci(i))


print(f(5))
print(my_fibonacci(5))

#Імпорт модуля  і декоратора (через рекурсію)

from functools import lru_cache


@lru_cache
def rec_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibonacci(n-1) + rec_fibonacci(n-2)


print(rec_fibonacci(100))