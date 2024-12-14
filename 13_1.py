class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}" if all_students else f"Group Number: {self.number}\nNo students in the group."

# Тестовий приклад
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
group = Group('PD1')

group.add_student(st1)
group.add_student(st2)
print(group)

# Перевірка пошуку студента
assert str(group.find_student('Jobs')) == str(st1), 'Test1'
assert group.find_student('Jobs2') is None, 'Test2'
assert isinstance(group.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

# Видалення студента
group.delete_student('Taylor')
print(group)  # Only one student

# Спроба видалення неіснуючого студента
group.delete_student('Taylor')  # No error!
