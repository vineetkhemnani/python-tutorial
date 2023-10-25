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
