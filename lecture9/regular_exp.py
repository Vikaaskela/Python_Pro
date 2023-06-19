#Task 1
#Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою 
#слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.

import re
string = input('string=')
result =re.findall(r'\w [Rb{1, }r]', string)
print(result)
if result:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Task 2
#Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

import re
string = input('string=')
result =re.split(r'^([0-9]{4}-)([0-9]{4}-)([0-9]{4}-)([0-9]{4}-)$', string)
print(result)
if result:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Task 4
#Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, 
# що містить лише літери та цифри.
import re
string = input('string=')
result =re.findall(r'^([\w|d]{2,10})$', string)
print(result)
if result:
  print("Yes, there is at least one match!")
else:
  print("No match")



