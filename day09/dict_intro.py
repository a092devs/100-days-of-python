programming_dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
# print(programming_dict["Function"])

# Adding new items to dictionary.
programming_dict["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# programming_dict = {}
# print(programming_dict)

# Edit an item in a dictionary
programming_dict["Bug"] = "A moth in your computer."
# print(programming_dict)

# Loop through dictionary
for key in programming_dict:
    print(key)
    print(programming_dict[key])