player_details = ["jordan", 25, "USA"]
additional_details = ["6ft6in", "chicago"]

print(player_details)
print(type(player_details))      # This is a list

print(player_details[0])         # First element
print(player_details[1])         # Second element
print(player_details[2])         # Third element

print(player_details * 3)        # Repeats the list 3 times
print(player_details + additional_details)  # Joins two lists together

player_details[1] = 26           # Changing the second element
print(player_details)

print("shush")
