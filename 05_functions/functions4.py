print("hi world")
name = input("What is your name? ")

# Lambda function for perimeter of a triangle
circ = lambda side1, side2, side3: side1 + side2 + side3
print(circ(2, 3, 4))

# Same function using def (optional)
def circ(side1, side2, side3):
    return side1 + side2 + side3

print(circ(2, 3, 4))


# -------------------------------
# Square numbers (normal loop)
# -------------------------------

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)


# -------------------------------
# Square using a function
# -------------------------------

def square_the_number(num):
    return num ** 2

print(square_the_number(7))

squares = []
for n in numbers:
    squares.append(square_the_number(n))

print(squares)


# -------------------------------
# Square using map()
# -------------------------------

squares = list(map(square_the_number, numbers))
print(squares)

# Another way (same result)
squares_map = map(square_the_number, numbers)
squares_list = list(squares_map)
print(squares_list)