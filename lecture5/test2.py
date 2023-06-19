class MySeq:

    def __init__(self, number):
        self.number = number

    def __getitem__(self, item):
        if 0 <= item < self.number:
            return item * 10
        raise IndexError()

    def __len__(self):
        return self.number


x = MySeq(10)
print(x[5])
print(x[9])
 
#for item in x:
#    print(item)