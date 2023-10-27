programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.", 
	"Function": "A piece of code that you can easily call over and over again.",
}

# adding an item to dictionary
programming_dictionary["Conditionals"] = "If-else are called conditionals as we can use multiple conditions through them"

# accessing an item from dictionary
# print(programming_dictionary["Bug"])

# printing the entire dictionary
# print(programming_dictionary)

# creating an empty dictionary
empty_dictionary={}

# wiping an existing dictionary
# programming_dictionary={}

# Edit an item in a dictionary
programming_dictionary["Bug"]= "A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # print(key) #prints all keys in the dictionary
    print(key+" : "+programming_dictionary[key]) # prints all the values in the dictionary

