#Task 4
#Реалізуйте свій аналог генераторної функції range().
def gen_item(range):
    index = 0
    while index < range:
        yield index
        index += 1
    
for item in gen_item(5):
    print(item)
