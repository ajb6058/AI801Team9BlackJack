import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
#import Blackjack_func <-- This will be where we store the different functions
import random

#BREAK OUT CARDS/DECK INTO ITS OWN FUNCTION
# The type of card
cards = 4 * ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
# The card value
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# Total Decks
total_decks = 3

# The deck of cards
deck = []
 
# Create the base deck
for x in range(0,total_decks):
    for card in cards:
        deck.append(cards_values[card])

print(len(deck))

#BREAK OUT INTO ITS OWN FUNCTION FOR BETS
bank = 1000.00
#how should we break out bets?
#bet logic and winnings (including bank updates) will need to be built in to logic below
#agent will need to be aware of their bank total and know when to quit

#BREAK OUT INTO ITS OWN FUNCTION FOR HOUSE DRAW
#Agent does not see house values until they stay, hit blackjack, or bust
house_draw = []
random.shuffle(deck)
house_draw.append(deck.pop(random.randrange(0,len(deck))))
random.shuffle(deck)
house_draw.append(deck.pop(random.randrange(0,len(deck))))

print(house_draw)
print(sum(house_draw))

if sum(house_draw) == 21:
    print("House Blackjack, Check your draw... if you have blackjack it is a push, if you do not it is a draw")


#BREAK OUT INTO ITS OWN FUNCTION FOR AGENT DRAW
agent_draw = []
random.shuffle(deck)
agent_draw.append(deck.pop(random.randrange(0,len(deck))))
random.shuffle(deck)
agent_draw.append(deck.pop(random.randrange(0,len(deck))))

print(agent_draw)
print(sum(agent_draw))
agent_choice = ""

if sum(house_draw) == 21 and sum(agent_draw) == 21:
    print("push")
elif sum(house_draw) == 21 and sum(agent_draw) != 21:
    print("you lose!")
elif sum(agent_draw) == 21:
    print("Blackjack! Let's see what the house has")
else:
    print("Would you like to Hit or Stay?")
    #Need to determine how to allow agent choice of hit or stay
    if agent_choice == "Hit":
        agent_draw.append(deck.pop(random.randrange(0,len(deck))))
        if sum(agent_draw) == 21:
            print("You've hit the max! Let's see what the house has")
        else:
            print("Would you like to Hit or Stay?")

#house rules state that dealer must draw until they reach at least 17. if 17 is reached they must stay
while sum(house_draw) < 17:
    house_draw.append(deck.pop(random.randrange(0,len(deck))))
print(sum(house_draw))

if sum(house_draw) == 21 and sum(agent_draw) == 21:
    print("Push, you get your original bet back")
elif sum(house_draw) == 21 and sum(agent_draw) != 21:
    print("you lose this round")
elif sum(house_draw) != 21 and sum(agent_draw) == 21:
    print("Blackjack! You win!")
elif sum(agent_draw) > 21:
    print("bust! You lose this round")
elif sum(house_draw) == sum(agent_draw):
    print("Push, you get your original bet back")
elif sum(house_draw) < sum(agent_draw):
    print("you win!")
elif sum(house_draw) < 21 and sum(house_draw) > sum(agent_draw):
    print("you lose")