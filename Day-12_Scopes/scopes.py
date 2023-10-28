# ################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength=2
#     print(potion_strength)

# drink_potion()
# print(potion_strength) => this line of code shows NameError: name 'potion_strength' is not defined
# as potion_strength is a Local Variable that exists only inside the scope of the function i.e. Local scope

# Global Scope
# player_health=10
# def drink():
#     potion_strength=2
#     print(player_health)

# drink()
# print(player_health)
# # the variable player_health is defined outside the function hence has a Global scope and
# # exists outside the function too

# There is no Block Scope in Python
game_level=3
enemies=["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy=enemies[0]
print(new_enemy)

# although new enemy is indented it does not have its own scope rather the scope of the parent
# i.e. here the global scope

## Modifying Global Scope


