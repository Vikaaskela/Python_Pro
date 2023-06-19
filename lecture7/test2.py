#Функція може містити всередині себе іншу функцію
'''
def power(exp):

    def inner(a):
        return a ** exp

    return inner


f = power(2)
print(f)
'''
'''
def power(exp):

    def inner(a):
        return a ** exp

    return inner


f = power(2)
for i in range(10):
    print(f(i))
'''
def calculate_pow(n):
    def calculate(number):
        return number ** n
    return calculate
f = calculate_pow(3)
number_one = f(2)
number_two = f(5)
print(number_one)
print(number_two)
