from datetime import datetime


class Human:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    def hundred_years(self):
        return "I will be hundred years old in", datetime.now().year + 100 - self.age

    def present(self):
        return f"Hi there! My name is {self.name} and i'm {self.age} years old. "


class Student(Human):
    def __init__(self, university, course, *args, **kwargs):
        self.uni = university
        self.course = course
        super().__init__(*args, **kwargs)

    def present(self):
        return f"{super().present()}" \
               f"I'm student of {self.uni}, I'm studying in {self.course} course."


class Employee(Human):
    def __init__(self, profession, salary, *args, **kwargs):
        self.profession = profession
        self.salary = salary
        super().__init__(*args, **kwargs)

    def present(self):
        return f"{super().present()}" \
               f"I'm a {self.profession} and my salary is {self.salary}$ "


class StudentEmployee(Student, Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


a = StudentEmployee("UFAR", 3, "Programmer", 3000000, "John", 18)
print(a.hundred_years())
print(a.present())
