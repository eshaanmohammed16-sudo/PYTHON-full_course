numbers = [21, 31, 1, 56, 6, 99]

# Function to check if a number is odd
def odd_filter(numb):
    return numb % 2 != 0

print(odd_filter(27))   # True (27 is odd)
print(odd_filter(16))   # False (16 is even)

# Filter out only the odd numbers from the list
filter_odds_function = list(filter(odd_filter, numbers))
print(filter_odds_function)