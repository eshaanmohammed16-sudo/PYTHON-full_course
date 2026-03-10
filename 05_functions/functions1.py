def greet():
    print("Hello")


input_no = int(input("Enter number of students: "))

def calculate_average(marks):
    if not marks:                 # If the list is empty
        print("No marks provided.")
        return
    total = sum(marks)            # Add all marks
    average = total / len(marks)  # Calculate average
    print("Average marks:", average)

marks = []

for i in range(input_no):
    marks.append(int(input("Enter marks: ")))

calculate_average(marks)