def format_name(f_name,l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name=="" or l_name=="":
        # early exit
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
	# .title() is used to capitalize the first letter of the string and convert rest to lower case
    formatted_l_name = l_name.title()
	# return the formatted string
    return f"{formatted_f_name} {formatted_l_name}"
    # print("Angela") => this print statement wont be executed as it is after return statement

# store the output of function in a variable
first_name=input("Enter first name: ")
last_name=input("Enter last name: ")
formatted_string = format_name(f_name=first_name,l_name=last_name)
print(formatted_string)

