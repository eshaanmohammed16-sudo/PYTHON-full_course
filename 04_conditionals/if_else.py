name = input("What is your name?")

print("Hi", name)

gender = input("What is your gender? ")
gender = gender.lower()        # Convert to lowercase for easy comparison

if gender == "male":
    print("Welcome Mr.", name)
else:
    print("Welcome Ms.", name)

print("Have a nice day", name)

###########################################################################################################################################################################

name = "akira"
gender = "male"

variable1 = input("What is your name? ")
variable2 = input("What is your gender? ")

variable1 = variable1.lower()   # Convert to lowercase for comparison
variable2 = variable2.lower()

# Check if the entered name matches the stored name
if variable1 == name:
    print("Welcome back, Akira!")
else:
    print("Hello, stranger!")

# Check if the entered gender matches the stored gender
if variable2 == gender:
    print("Correct")
else:
    print("wyoab")

print("Have a nice day", variable1)