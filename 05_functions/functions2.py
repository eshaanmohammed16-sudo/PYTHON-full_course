def greet():
    print("Hello, World!")

greet()
greet()
greet()
greet()
greet()


def collect_student_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    mobile = input("Enter your mobile: ")

    # Split name into first and last
    parts = name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else "Not Provided"

    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Age:", age)

collect_student_details()


# Function with required parameters
def display_details(name, age, email, mobile):
    print("name :", name)
    print("age  :", age)
    print("email:", email)
    print("mobile:", mobile)

display_details("John Doe", 20, "jdoe@gmail.com", "123-456-7890")
display_details("Jane Smith", 22, "jsmith@gmail.com", "098-765-4321")


# Function with default parameters
def display_details(name, age, email="eshaan.mohammed19@gmail.com", mobile="Not Provided"):
    print("name :", name)
    print("age  :", age)
    print("email:", email)
    print("mobile:", mobile)

display_details("Alice", 19)   # Works because defaults are provided