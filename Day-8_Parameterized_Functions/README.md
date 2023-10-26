## Parameterized functions
```
def functionName(name):
	ToDo with name
```
- name = "Vineet" <br>
&uarr;&emsp;&emsp;&emsp;&emsp;&uarr;<br>
params&emsp;args
```

def greet_with_input(name):   #name is a parameter
	print(f"Hi {name}")
	print(f"Hello {name}")
	print(f"How you doing {name}")

greet_with_input("Vineet")
#                 Vineet is an argument
```

### Dynamic input from user as parameter to the function
```
name=input("Whats your name?")
def greet_with_input(name):
	print(f"Hi {name}")
	print(f"Hello {name}")
	print(f"How you doing {name}")

greet_with_input(name)
```
- In the above code the user asks for name as input then displays the statements according to the entered input

### More than one parameter
```
name=input("Whats your name? ")
location=input("Whats your location? ")
def greet_with_input(name,location):
	print(f"Hi {name}")
	print(f"Hello {name}")
	print(f"How you doing {name}")
	print(f"Whats it like in {location}")

greet_with_input(name,location)
```

### Positional Arguments
```
def my_function(a,b,c):
    # Do something

my_function(1,2,3)
```
- Order of arguments matters as 1st argument will be assigned to 1st param, 2nd argument to second param and so on
- Above function sets a=1,b=2,c=3

### Keyword arguments
- Instead of vaguely defining arguments, we use parameter names inside arguments<br>
For ex:-
```
def my_function(a,b,c):
    # Do something

my_function(a=1,b=2,c=3)
```
- Now even if we write ```my_function(b=2,c=3,a=1)```, the arguments are assigned according to param names instead of position