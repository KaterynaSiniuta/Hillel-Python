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


class GroupLimitError(Exception):
    """Користувацький виняток для перевищення ліміту студентів у групі"""
    def __init__(self, message="Group cannot have more than 10 students"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
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
st3 = Student('Male', 21, 'John', 'Doe', 'AN146')
st4 = Student('Female', 22, 'Jane', 'Doe', 'AN147')
st5 = Student('Male', 23, 'Mike', 'Smith', 'AN148')
st6 = Student('Female', 24, 'Anna', 'Brown', 'AN149')
st7 = Student('Male', 20, 'Tom', 'Hanks', 'AN150')
st8 = Student('Female', 19, 'Emma', 'Stone', 'AN151')
st9 = Student('Male', 26, 'Chris', 'Evans', 'AN152')
st10 = Student('Female', 27, 'Scarlett', 'Johansson', 'AN153')
st11 = Student('Male', 28, 'Robert', 'Downey', 'AN154')

group = Group('PD1')

# Додавання студентів
try:
    group.add_student(st1)
    group.add_student(st2)
    group.add_student(st3)
    group.add_student(st4)
    group.add_student(st5)
    group.add_student(st6)
    group.add_student(st7)
    group.add_student(st8)
    group.add_student(st9)
    group.add_student(st10)
    # Спроба додати 11-го студента
    group.add_student(st11)
except GroupLimitError as e:
    print(f"Error: {e}")

# Вивід групи
print(group)
