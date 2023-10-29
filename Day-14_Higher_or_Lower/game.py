from art import logo
from art import vs
print(logo)
# check who has more followers
def checkFollowers(account_a,account_b,guess):
    """Take the user guess and follower counts and returns if they got it right"""
    if account_a['follower_count']>account_b['follower_count']:
        return  guess == "a"
    else:
        return guess=="b"

from game_data import data
import random

score=0
account_b=random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)

    
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")

    print(vs)

    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    guess=input("Who has more followers?Type 'A' or 'B': ").lower()
        
    is_correct= checkFollowers(account_a=account_a, account_b=account_b,guess=guess)

    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue=False
        print(f"Sorry, thats wrong. Final score: {score}")

