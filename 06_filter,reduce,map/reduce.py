from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to find the maximum value
def max_finder(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

results = reduce(max_finder, numbers)
print(results)