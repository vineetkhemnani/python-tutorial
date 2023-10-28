## Scopes in Python
### Local vs Global Scope
#### Local Scope
```
def drink_potion():
    potion_strength=2
    print(potion_strength)

drink_potion()
print(potion_strength) => this line of code shows NameError: name 'potion_strength' is not defined
```
- as potion_strength is a Local Variable that exists only inside the scope of the function i.e. Local scope

#### Global Scope
- the only difference between local scope and global scope is where you create or where you define your variables
```
player_health=10
def drink():
    potion_strength=2
    print(player_health) => 10

drink()
print(player_health) => 10
```
- the variable player_health is defined outside the function hence has a Global scope and exists outside the function too

### Namespaces
- The above concept of global and local scope not only applies to variables but also functions
- This is called **NAMESPACE**
- Anything that we give a name too has a ***namespace***

**THERE IS NO SUCH THING AS BLOCK SCOPE IN PYTHON**

- Blocks like **if, while, for** with colons and indentation dont count as creating a local scope

### Modifying global scope through local scope
```
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function{enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```
- ***enemies = 1*** and ***enemies = 2*** create two entirely different variables independent of each other
- this is why it printed = 1 first then equal to 2 because both variables are different

- Terrible idea to call local and global variables the same name

```
enemies = 1

def change_enemies():
    # enemies below refers to a different variable than enemies outside local scope
    enemies+=1    # => error on this line
    print(f"enemies inside function: {enemies}")
```
- In the above example, editor thinks we are trying to access a local variable inside change_enemies() function but there is none present hence the error

- In order to access the global variable we have to explicitly define that we are trying to use a global variable
```
enemies = 1

def change_enemies():
    global enemies
    enemies+=1
    print(f"enemies inside function: {enemies}")
```
- The line ```global enemies``` defines that we are trying to access a global variable not a local one
- You probably should not do this as this may result in bugs and makes code more error prone.
- **Reading global variables** is okay but it is ***not a good practice*** to change global variables in local scope
- Instead of modifying enemies inside function, we can use a return  ```enemies+1``` and assign it to a new variable
```
enemies = 1

def change_enemies():

    print(f"enemies inside function: {enemies}")
    return enemies+1

enemies=change_enemies()
print(f"enemies outside function: {enemies}")
```

## Global Const Naming Convention
- All upper case naming condition is followed
```
PI = 3.14159
URL = "https://www.google.com"
```

