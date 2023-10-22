## Operators in python
- +,-,*,/
- / => division in float
- // => division in floor (returns floor of division)
- ** => power 
- ```2 ** 3``` => returns 8
- round((expression),place)
for ex:-
```
print(round((8/3),1))
# rounds off ABOVE code to 1 decimal place
print(round((8/3),2))
# rounds off ABOVE code to 2 decimal place
```
- Another way to round off two decimal
```
formatted_num="{:.2f}".format(num)
```
## Shorthands
- result=result/2 can be written as result/=2
- also result=result+2 can be written as result+=2
and so on

## Template literals or f-strings(formatted strings)
```
score=0
height=1.2
isWinning=True
print(f"score is {score}, height is {height}, isWinning is {isWinning}")
```

## Conditionals in python
Syntax
```
if height>120:
	print("yay you can sit in the rollercoaster")
else:
    print("Sorry! you cant ride in the rollercoaster")
	print("Wear taller pair of shoes")
```

## Nested if-else and elif
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height>120:
	print("Yay!!! you can sit in the rollercoaster")
	age=int(input("Enter age: "))
	if age<12:
		print("Ticket price is $5")
	elif age>12 and age<=18:
		print("Ticket price is $7")
else:
	print("Sorry! you cant ride in the rollercoaster")
	print("Wear taller pair of shoes")
```

## Indentation in if-else
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0


if height>120:
	print("Yay!!! you can ride in the rollercoaster")
	age=int(input("Enter age: "))
	if age<12:
		bill=5
		print("Child ticket is $5")
	elif age>12 and age<=18:
		bill=7
		print("Youth ticket is $7")
	else:
		bill=12
		print("Adult ticket is $12")
	
	wants_photo=input("do you want photos? type Y or N")
	if wants_photo=="Y":
		bill+=3
		print(f"Your bill is ${bill}")
else:
	print("Sorry! you cant ride in the rollercoaster")
	print("Wear taller pair of shoes")
```

## Inbuilt functions
- lower() => changes the entire string to lowercase
- count("") => counts the number of times a character specified in brackets occurs
- count() is **case sensitive**

## Randomizing numbers
- import random
- random.randint(a,b) - gives a random integer between a and b (a and b inclusive)
- random.random() - random float between 0 and 1 (1 excluded)

## Modules in python (ex. random)
- Long piece of code divided into smaller chunks where each chunk is responsible for a different bit of functionality of program. These chunks are called **MODULES**

### Creating modules
- main.py is the entry point of our code
- create a new file with ```.py``` extension and import it in main file
- use ```modulename.variable_name``` to access variable

## Lists in python
```
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Conneticuit", "Maryland", "South Carolina", "New Hampshire" "Virginia", "North Carolina"]
# order is very important as order is index
print(states_of_america[0])
# prints Delaware
```
- A positive index means from the starting index of the list
for ex.
```print(states_of_america[2])```=> prints 2nd from the starting of the list
- A negative index means from the ending of the list
```print(states_of_america[-2])``` => prints 2nd from the ending of the list

```
print(states_of_america[2]) #prints Delaware
print(states_of_america[-2]) #prints Virginia
```

### Changing data of list
- states_of_america[1] = "Pencilvania"
Above code changes the 1st index from "Pennsylvania" to Pencilvania

### Appending data to the list
- states_of_america.append("Hawaii") - adds "Hawaii" to the end of the list

### Extending the list (append an array)
- states_of_america.extend(["South Dakota, New York"]) - adds a list to the end of the states_of_america

### str.split("reg_exp")
- splits a string into a list based on the reg_exp
for ex:-
```
intro = "Hello,My,Name,is,Vineet"
intro_list=intro.split(",")
print(intro_list)
```
Above output is
```['Hello', 'My', 'Name', 'is', 'Vineet']```

### Nested lists
- fruits = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
- vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

- dirty_dozen=[fruits,vegetables] => 2 lists inside a list
o/p- [['strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

## Loops in Python
### for loop
```
fruits=[
	"apple",
	"banana",
	"cherry",]
for fruit in fruits:
	print(fruit)
	print(fruit+" "+"pie")
	print(fruits) #prints thrice coz indentation means inside loop
print(fruits) #prints once coz outside loop
```
### for loop within range
for number in range(a,b):
	print(number)
```
for number in range(1,10):
	print(number)
```
- Above code prints number from 1 to 9 (Excluding 10)

- If you want to specify the step-size or increment size, you need to specify a 3rd parameter in range
```
for number in range(0,10,3):
	print(number)
```
- Here "3" specifies the step size as in increment each time by 3
- So the loop runs for 1,4,7 i.e. **three times**

## Some more random functions
- random.choice(list) - chooses a random element from the list
- random.shuffle(list) - shuffles the contents of the list in random order