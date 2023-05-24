class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def __iadd__(self, other: Student):
        if not isinstance(other, Student):
            return NotImplemented
        if other in self.students:
            raise ValueError()

        self.students.append(other)
        return self

    def __getitem__(self, item):
        return self.students[item]

    def __len__(self):
        return len(self.students)


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

gr_1 = gr[::2]
gr_2 = gr[1::2]
'''
for item in gr_1:
    print(item)
print('*' * 10)
for item in gr_2:
    print(item)

print(len(gr))
'''
for item in gr:
    print(item)