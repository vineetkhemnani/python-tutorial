from art import logo
import random

EASY_LVL_TURNS = 10
HARD_LVL_TURNS = 5
print(logo)
def check_answer(guess, number,turns):
    """checks answer against guess and returns number of turns"""
    if guess > number:
        print(f"Too high")
        return turns-1
    elif number > guess:
        print(f"Too low")
        return turns-1
    else:
        print(f"You won. Correct answer is {number}")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number=random.randint(1,100)
    print(f"Number is {number}")
    def difficult_lvl():
        lvl=input("Enter 'hard' for hard diffculty, 'easy' for easy diffculty: ")
        if lvl=='hard':
            turns = HARD_LVL_TURNS
        elif lvl=='easy':
            turns = EASY_LVL_TURNS
        return turns
    turns=difficult_lvl()
    print(f"You have {turns} attempts remaining")

    guess=0
    while guess != number:
        guess=int(input("Submit a guess: "))
        turns=check_answer(guess,number,turns)
        print(f"You have {turns} turns remaining")
        if turns == 0:
            print("Oops!! You have no turns remaining")
            return
        elif guess!=number:
            print("Guess again")
game()