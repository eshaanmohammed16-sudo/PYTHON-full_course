# print(dir(str))
string1 ="python" #immutable-cannot be changed
print(string1)#original string remains same
print(string1.capitalize()) #capital P
print(string1) #original string remains same
string2="PYTHON"
print(string1.casefold() == string2.casefold())
#casefold used to compare strings ignoring case sensitivity
#output: True
print(string1.center(50))#centers the string in a space of 50 characters
print(string2.center(50,'*'))#centers the string in a space of 50 characters with * as fill character
string3="python programming language"
# print(string3.count('a')) #counts number of occurrences of 'a' in the string
print(string3.endswith("python")) #checks if string ends with given substring -ends with boolean output
print(string3.endswith("language   ")) #checks if string ends with given substring - ends with boolean output
# print(string3.startswith("   python")) #checks if string starts with given substring - starts with boolean output
# print(string3.startswith("python")) #checks if string starts with given substring - starts with boolean output
# print(string3.find("programming")) #returns starting index of substring if found else -1
# print(string3.find("adr")) #returns starting index of substring if found else -1
#-1 means substring not found
#print(string3.index(","))
#print(string3.index("programming")) #returns starting index of substring if found else raises ValueError
#print(string3.index("adr")) #returns starting index of substring if found else raises ValueError
#ValueError means substring not found
string4="10"#can convert to number
string5="a" #cannot convert to number
# print(string4)
# print(type(string4))
# print(string4.isdigit()) #checks if all characters in string are digits - boolean output
# print(string4.isdecimal()) #checks if all characters in string are decimals - boolean output
# print(string4.isnumeric()) #checks if all characters in string are numerics - boolean output

# print(string5)
# print(type(string5))    
# print(string5.isdigit()) #checks if all characters in string are digits - boolean output
# print(string5.isdecimal()) #checks if all characters in string are decimals - boolean output
# print(string5.isnumeric()) #checks if all characters in string are numerics - boolean output
# #digits, decimals and numerics are same for basic characters like 0-9
# num3=int(string4) #converts string to integer
# print(num3)
# num4=float(string4) #converts string to float
# print(num4)
# num5=int(string5) #raises ValueError as string cannot be converted to number
# print(num5)

words=string3.split(" ") #splits string into list of words based on given delimiter
print(words)
#OUTPUT: ['python', 'programming', 'language']
# print(string3) #original string remains same
print(type(words)) #list

print(string3)
print(string3.strip()) #removes leading and trailing whitespaces # only leading and trailing spaces
string6="                       python programming lang uage                 "
print(string6)
print(string6.strip()) #removes leading and trailing whitespaces # only leading and trailing spaces

print(string2)
print(string2.swapcase()) #swaps case of each character

print("shush")