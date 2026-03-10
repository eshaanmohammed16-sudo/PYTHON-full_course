# Functions with keyword arguments
def display_details(name, age, email, mobile):
    print("name :", name)
    print("age  :", age)
    print("email:", email)
    print("mobile:", mobile)

display_details("John Doe", 20, "jdoe.gmail.com", "123-456-7890")

# Using keyword arguments (order doesn't matter)
display_details(
    mobile="098-765-4321",
    email="jsmith.gmail.com",
    age=22,
    name="Jane Smith"
)


# Functions with default arguments
def new_emp(name, dept, position):
    print(f"{name} works in {dept} as a {position}")

new_emp("Alice", "HR", "Manager")
new_emp(position="Developer", name="Bob", dept="IT")


# Function with variable number of arguments (*args)
def emp_seperation(*arguments):
    print(arguments)
    print(type(arguments))

emp_seperation("salary", "bonus", "pf", "insurance", "leave_encashment")
emp_seperation("salary", "bonus")