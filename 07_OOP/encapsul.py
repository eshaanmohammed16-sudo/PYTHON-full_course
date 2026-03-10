class Student:
    def __init__(self, aadharid):
        self.__aadharid = aadharid   # private attribute

st1 = Student(1234)

# Correct way to access a private variable (name‑mangling)
print(st1._Student__aadharid)