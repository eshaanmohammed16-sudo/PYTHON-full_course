# List of names
names = ["Neel", "Aryan", "Vimush", "Eshaan", "Akira"]

# Function to convert a name to uppercase
def convert_uppercase(name):
    return name.upper()

# Test the function
answer = convert_uppercase("Neel")
print(answer)

# Use map() to convert all names to uppercase
convert_uppercase_map = list(map(convert_uppercase, names))
print(convert_uppercase_map)
print(convert_uppercase("Sulaiman"))