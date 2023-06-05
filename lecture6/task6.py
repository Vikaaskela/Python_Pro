#Task 6
#Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до
#вказаної вами величини.
'''
def func(n):
    index = 0
    a, b = 0, 1
    while index < n:
        yield b
        a, b = b, b + a
        index += 1

x = (i ** 3 for i in range(2,20))
for item in x:
    print(item)
''' 
  
n = int(input('n='))
x = (i ** 3 for i in range(2, n))
y = list(x)
print(y)
'''
def gen_cube(n):
    for i in range(2, n):
        yield i ** 3
    print(i)
'''