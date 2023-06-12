#Task 3
#Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів 
#отриманого списку.
'''
def func_1(user_func):
    def func_2(num_list):
        return sum(user_func(item) for item in num_list)
    return func_2

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4]

func = func_1(square)

print(func(my_list))
'''
#Одна функція до різних списків
def get_items(func):
    def inner(sequence):
        for index, item in enumerate(sequence):
            sequence[index] = func(item)
        return sum(sequence)
    return inner


f = get_items(lambda item: item ** 2)
x_1 = [1, 3, 5, 7, 9]
x_2 = [2, 4, 6, 8, 10]
print(f(x_1))
print(x_1)

print(f(x_2))
print(x_2)
#До однієї послідовності застосовувати різні функції
def get_items(sequence):
    def inner(func):
        for index, item in enumerate(sequence):
            sequence[index] = func(item)
        return sum(sequence)
    return inner

x = [1, 3, 5, 7, 9]
f = get_items(x)
print(f(lambda item: item ** 2))
print(x)

print(f(lambda item: item ** 3))
print(x)

