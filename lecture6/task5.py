#Task 5
#Напишіть генераторну функцію, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана 
#параметром цієї функції.
def prime_numbers(number):
    for n in range(2, number):
        for i in range(2, n - 1):
            if n % i == 0:
                break
        else:
            yield n


for i in prime_numbers(100):
    print(i)