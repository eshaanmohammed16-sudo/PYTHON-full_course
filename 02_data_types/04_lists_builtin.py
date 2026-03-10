# print(dir(list))  # Shows all list functions

# List of common list operations
list_ops1 = ["append", "clear", "copy", "count", "extend", "index", "insert"]
list_ops2 = ["remove", "reverse", "sort"]

print(list_ops1)

list_ops1.append("pop")        # Adds "pop" to the end of the list
print(list_ops1)

# list_ops1.clear()            # Clears the entire list (keep commented)
print(list_ops1)

list1 = [1, 2, 3, 4, 67, 89]
print(list1)

# list1.clear()                # Clears list1 (keep commented)
print("List after clear:")
print(list1)

print(list1.count(1))          # Counts how many times 1 appears in the list

list_ops1.extend(list_ops2)    # Adds all elements of list_ops2 to list_ops1
print(list_ops1)               # Modified list
print(list_ops2)               # Unchanged

print(list_ops1.index("extend"))   # Finds index of "extend"

list_ops1.insert(2, "new_item")    # Inserts at index 2
print(list_ops1)

popped_item = list_ops1.pop()      # Removes and returns last item
print("Popped item:", popped_item)
print(list_ops1)

list_ops1.remove("new_item")       # Removes first occurrence of "new_item"
print(list_ops1)

list_ops1.reverse()                # Reverses the list
print(list_ops1)

list_ops1.sort()                   # Sorts alphabetically
print(list_ops1)

list_numbers = [5, 2, 9, 1, 5, 6]
list_numbers.sort()                # Ascending order
print(list_numbers)

list_numbers.sort(reverse=True)    # Descending order
print(list_numbers)

student = ["Ab", 17, "B", "teacher"]
student_copy = student.copy()      # Shallow copy
print(student)
print(student_copy)

student.clear()                    # Clears original list
print("Original list after clear:", student)
print("Shallow copy of the list:", student_copy)

print(student_copy[1])             # Accessing index 1 from the copy

from copy import deepcopy
student_copy_deep = deepcopy(student_copy)   # Deep copy
print("Deep copy of the list:", student_copy_deep)

student_copy.clear()               # Clearing shallow copy
print("Shallow copy after clear:", student_copy)
print("Deep copy remains unchanged:", student_copy_deep)

print("shush")