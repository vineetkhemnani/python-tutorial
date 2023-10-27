import os


#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

prompt='yes'
bidders={}
while prompt == 'yes':
	name=input("Name of bidder: ")
	bid=int(input("What is your bid? $"))
	prompt=input("Are there any other bidders: Type 'yes' or 'no': ")
	bidders[name]=bid
	os.system('cls')

max_bid=0
winner=""
for key in bidders:
	if max_bid<bidders[key]:
		max_bidder=bidders[key]
		winner=key

print(f"Winner is {winner}")
		
