#Task 3
#Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів 
#отриманого списку.
def func_1(user_func):
    def func_2(num_list):
        return sum(user_func(item) for item in num_list)
    return func_2

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4]

func = func_1(square)

print(func(my_list))



