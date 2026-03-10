class Student:
    def __init__(self, name, age, city, courses, marks):
        self.name = name
        self.age = age
        self.city = city
        self.courses = courses
        self.marks = marks

    def calculate_average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(avg)


st1 = Student("Nag", "15", "Hyd", "MPC", [67, 68, 89])

print(st1.name)
print(st1.age)
st1.calculate_average()