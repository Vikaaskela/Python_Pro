class Student:

    def __init__(self, name: str, surname: str, date_of_birth: str):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.students))


group = Group('Python Pro')
student_1 = Student('Ivan1', 'Ivanov1', '12.03.2001')
student_2 = Student('Ivan2', 'Ivanov2', '12.03.2002')
student_3 = Student('Ivan3', 'Ivanov3', '12.03.2003')
student_4 = Student('Ivan4', 'Ivanov4', '12.03.2004')
student_5 = Student('Ivan5', 'Ivanov5', '12.03.2005')

group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)
group.add_student(student_4)
group.add_student(student_5)

print(group)