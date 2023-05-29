class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class GroupIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            self.index += 1
            return self.items[self.index - 1]
        raise StopIteration()


class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def __iadd__(self, other):
        self.students.append(other)
        return self

    def __iter__(self):
        return GroupIterator(self.students)
    
    



st_1 = Student('Ivan1', 'Ivanov1')
st_2 = Student('Ivan2', 'Ivanov2')
st_3 = Student('Ivan3', 'Ivanov3')
st_4 = Student('Ivan4', 'Ivanov4')
st_5 = Student('Ivan5', 'Ivanov5')
st_6 = Student('Ivan6', 'Ivanov6')

gr = Group('Python Pro')
gr += st_1
gr += st_2
gr += st_3
gr += st_4
gr += st_5
gr += st_6

#it = iter(gr)
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

#it = iter(gr)
#while True:
#    try:
#        print(next(it))
#    except StopIteration:
#        break

for student in gr:
    print(student)