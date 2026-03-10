numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

for val in range(1, 22):
    print(val)          # Does not include 22

for val in range(5):
    print(val)          # 0 → 4

for val in range(2, 11, 2):
    print(val)          # Step of 2

for val in range(10, 0, -1):
    print(val)          # 10 → 1 backwards

for val in range(1, 6):
    print(val)
else:
    print("Loop completed")   # Runs only if loop finishes normally


# Break example
NUMBERS = [10, 20, 30, 40, 50]
for num in NUMBERS:
    if num % 2 == 0:
        print("Found EVEN", num, "stopping the loop.")
        break


# Continue example
numbers = [1, 3, 5, 7, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print("Found EVEN", num)
        print("Found odd", num)   # Keeping your original logic
    else:
        print(num)


# String formatting
name = "john"
age = 25

print(name + " is a good boy")
print("He is " + str(age) + " years old")
print("{} is a good boy".format(name))
print(f"{name} is a good boy and he is {age} years old")


# Continue to filter even numbers
numbers = [1, 2, 3, 4, 5]
even_list = []

for num in numbers:
    if num % 2 != 0:
        continue
    even_list.append(num)

print(even_list)