#Task 8
#Реалізуйте генераторну функцію для генерації послідовності дат. Початкова та кінцеві дати мають бути 
#задані параметрами цієї функції.
'''
def data(n):
    a = 1
    statr, stop = 1, 31
    while a < n:
        yield a 
        a += 1
    
for item in data(31):
    print(item)
'''
from datetime import datetime, timedelta

def date_range(start, stop):
    current = start
    while current <= stop:
        yield current
        current += timedelta(days=1)


str_start_date = tuple(map(int, input('yyyy-mm-dd\n').split('-')))
str_end_date = tuple(map(int, input('yyyy-mm-dd\n').split('-')))

start_date = datetime(str_start_date[0], str_start_date[1], str_start_date[2])
end_date = datetime(str_end_date[0], str_end_date[1], str_end_date[2])

for gen_date in date_range(start_date, end_date):
    print(gen_date)
