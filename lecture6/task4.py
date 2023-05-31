#Task 4
#Реалізуйте свій аналог генераторної функції range().
def gen_range(a):
    index = 0
    while index < a:
        yield index
        index += 1
    
for item in gen_range(5):
    print(item)
