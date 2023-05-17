#Відсутність дублікатів в add student і перевірити в remove student чи існує студент
class Student:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
       
    def __str__(self):
        return f'{self.surname} {self.name}'


class Group:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return '\n'.join(map(str, self.students))



student_1 = Student('Ivan', 'Ivanov')
student_2 = Student('Stepan', 'Stepanenko')
student_3 = Student('Roman', 'Romanenko')
student_3 = Student('Roman', 'Romanenko')


group = Group()
group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)

print(group)