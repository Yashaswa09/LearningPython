# Define a dictionary 'marks' with student names as keys and their marks as values
marks = {
    "Yashaswa": 100,
    "kunal": 95,
    "Jevansh": 88,
    "Harsh": 85
}
# In Dict {} are used to make Dictionary

# Print the dictionary and its type
print(marks, type(marks))

# Print all items (key-value pairs) in the dictionary
print(marks.items())
# marks.items() command is used to view items in the above dictionary

# Print all keys in the dictionary
# Note: The correct method is 'keys()', not 'key()'
print(marks.keys())

# Print the dictionary again
print(marks)

# Print all values in the dictionary
print(marks.values())

# Update the dictionary: change 'Yashaswa' marks to 105 and add a new entry 'Kelo': 55
marks.update({"Yashaswa": 105, "Kelo": 55})
print(marks)

# Get the value for the key 'Yashaswa'
print(marks.get("Yashaswa"))

# Print the dictionary again
print(marks)

# Remove the entry with key 'Harsh'
marks.pop("Harsh")

# Remove and return the last inserted key-value pair
# Note: popitem() does not take any arguments; this line will cause an error
# marks.popitem("88")  # Incorrect usage

# Delete the entry with key 'Harsh'
# Note: 'Harsh' has already been removed above, so this will cause a KeyError
# del marks["Harsh"]  # Will cause error if 'Harsh' is already removed

# Remove all items from the dictionary
marks.clear()
print(marks)
