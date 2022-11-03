from datetime import datetime


class Human:
    def __init__(self, name, surname, age, height, weight, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def count_age(self):

        this_date = datetime.now()
        year = this_date.year
        sample = 100

        a = f"You will be 100 years old in {year + (sample - self.age)}."
        return a

    def optimal_weight(self):
        men = 50 + (0.91 * (self.height - 152.4))
        women = 45.5 + (0.91 * (self.height - 152.4))

        if self.gender == "male":
            return f"Your optimal weight is: {men}kg."
        else:
            return f"Your optimal weight is: {women}kg."


class Student(Human):

    def __init__(self, university, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uni = university
        self.marks = []

    def avg_mark(self):
        mark = sum(self.marks) / len(self.marks)
        return mark

    def add_marks(self, grade):
        self.marks.append(grade)

    def present(self):
        return f"Hey! I'm {self.name} {self.surname}. I'm a student of {self.uni}. My height is {self.height}cm and " \
               f"weight is {self.weight}kg. " \
               f"My marks are {self.marks} and the average of these is {self.avg_mark()}"


art = Student("Stanford", "Naomi", "Johns", 18, 168, 60, "female")
art.add_marks(9)
art.add_marks(8)
art.add_marks(7)

print(art.marks)
print(art.avg_mark())
print(Student.present(art))
print(Student.count_age(art))
print(Student.optimal_weight(art))
