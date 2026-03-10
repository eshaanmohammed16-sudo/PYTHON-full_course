# print(dir(tuple))

tuple1=("John",25,"USA")
print(tuple1)
print(type(tuple1))

print(tuple1.count(25)) #counts how many times 25 occurs in the tuple
print(tuple1.index("USA")) #returns the index of the first occurrence of "USA"
#tuples are read-only data structures
# tuple1[1]=30 #this will raise an error becuase tuples are immutable(cannot be changed)

print("shush")
