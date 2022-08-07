# import sys
# import numpy
# import matplotlib
# import pandas
# import sklearn
import tensorforce
import kerasRL
import os
import Blackjack_func
import random

##############################################################################
#                           TO DO
# --Create a "Initial Hand" class -- Not sure if this is actually doable...
#   --Initial hand can be used for both house and agent, but may be tricky if they are not their own functions, 
#     this will require additional testing
# --Create a "Bet" class?
#
# --Create an agent
#   --Currently, the "agent" values are hard-coded, but an agent will be needed to play the game
# --Create a script for testing/learning
# --Look for alternative solution for nested if-else statements (dynamic based on deck size preferred)
# --Nest the while loop to continue to run and shuffle the deck
#   --Run a test to see how many games are played before busting
# --Run a test with hitting every time
# --Run a test with different bet values as the default
##############################################################################


initdeck = Blackjack_func.Deck()
deck = initdeck.deck()

#create a counter to keep track of how many games were played
gameCounter = 0

#BREAK OUT INTO ITS OWN FUNCTION FOR BETS
#From proposal, we decided that the user would start out with $100 in the bank
bank = 100.00
#how should we break out bets?
bet_values = [1.00,2.00,5.00,10.00]
min_bet_value = 1.00
max_bet_value = 10.00

#we need to give the agent the ability to choose their bet
default_bet_value = 2.00

## Number of winds and losses
wins = 0
losses = 0

#Initiatlizing agent continue playing
AgentContinue = 'Y'

#currently utilizing a while loop for testing. If Bank goes below 1.00 or deck goes below a summed value of 60, stop
#When the deck class is created, we can create a nested while loop
#The outer loop will check for bank value, the inner loop will check for deck size and re-shuffle when deck goes below a summed value of 60
while bank >= 1.00 and sum(deck) >= 60 and AgentContinue == 'Y':
    
    #Agent choice each new turn, currently set to default value for testing
    bet = default_bet_value
    #bet logic and winnings (including bank updates) will need to be built in to logic below
    #agent will need to be aware of their bank total and know when to quit
    
    
    #BREAK OUT INTO ITS OWN FUNCTION FOR HOUSE DRAW
    #Agent does not see house values until they stay, hit blackjack, or bust
    #The House Draw is the initial hand for the dealer
    house_draw = []
    #re-shuffling each time to ensure randomness in draw
    random.shuffle(deck)
    #Using pop to remove the last value in the deck to ensure that it cannot be selected again
    house_draw.append(deck.pop(random.randrange(0,len(deck))))
    random.shuffle(deck)
    house_draw.append(deck.pop(random.randrange(0,len(deck))))
    
    
    print(house_draw)
    print(sum(house_draw))
    
    if sum(house_draw) == 21:
        print("House Blackjack, Check your draw... if you have blackjack it is a push, if you do not it is a draw")
    elif sum(house_draw) == 22:
        #because it is possible to draw 2 aces in a single hand, we want to force one of those aces to be a 1 (since ace value by default is 11, but can be 1)
        house_draw.insert(1,1)
    
    
    #BREAK OUT INTO ITS OWN FUNCTION FOR AGENT DRAW
    #The Agent Draw is the initial hand for the Agent
    agent_draw = []
    random.shuffle(deck)
    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
    
    random.shuffle(deck)
    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
    
    print(agent_draw)
    print(sum(agent_draw))
    
    #setting variable for agent choice of "Hit" or "Stay"
    agent_choice = "Hit" #Scenario if the agent always hit
    
    #setting variable for agent choice for converting ace value to 1 "Y" or "N"
    agent_choice_ace = "Y" #Scenario if the agent always converted ace to 1
    
    #Initializing agent blackjack status. 
    blackjack_status = 'N'
    
    #Initializing agent bust status.
    bust = 'N'
    
    
    
    #START GAME AGENT CHOICE LOGIC
    if sum(agent_draw) == 22:
        agent_draw.insert(1,1)
    
    if sum(house_draw) == 21 and sum(agent_draw) == 21:
        print("") #Unsure if this should be converted to a break. The logic needs to be in place so that resulting logic can work properly
    elif sum(house_draw) == 21 and sum(agent_draw) != 21:
        print("") #Unsure if this should be converted to a break. The logic needs to be in place so that resulting logic can work properly
    elif sum(agent_draw) == 21:
        print("Blackjack! Let's see what the house has")
        blackjack_status = 'Y' #updating to 'Y' because agent_draw has blackjack
    else:
        #The following nested if-else statements check for whether the agent would like to hit or stay
        #There are 16 layers currently based off of 3 decks: 
            #There are 12 possible aces in the deck and if the initial draw is an ace and a 2 then the rest of the aces are drawn and then remaining 2s until 21, that is 16 possible hands
        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
        #Need to determine how to allow agent choice of hit or stay
        if agent_choice == "Hit":
            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
            #check
            for value in agent_draw:
                if value == 11:
                    print("Would you like to change this to a 1?")
                    #Allow agent to choose yes or no then update accordingly
                    if agent_choice_ace == 'Y':
                        #Currently, updating all aces in hand to 1. NEED TO DETERMINE A WAY TO ONLY UPDATE LATEST DRAW
                        agent_draw = [1 if i == 11 else i for i in agent_draw]
            if sum(agent_draw) == 21:
                print("You've hit the max without going over! Let's see what the house has")
            elif sum(agent_draw) > 21:
                bust = 'Y'
            else:
                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                if agent_choice == "Hit":
                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                    for value in agent_draw:
                        if value == 11:
                            print("Would you like to change this to a 1?")
                            #Allow agent to choose yes or no
                            if agent_choice_ace == 'Y':
                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                if sum(agent_draw) == 21:
                    print("You've hit the max without going over! Let's see what the house has")
                elif sum(agent_draw) > 21:
                    bust = 'Y'
                else:
                    print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                    if agent_choice == "Hit":
                        agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                        for value in agent_draw:
                            if value == 11:
                                print("Would you like to change this to a 1?")
                                #Allow agent to choose yes or no
                                if agent_choice_ace == 'Y':
                                    agent_draw = [1 if i == 11 else i for i in agent_draw]
                    if sum(agent_draw) == 21:
                        print("You've hit the max without going over! Let's see what the house has")
                    elif sum(agent_draw) > 21:
                        bust = 'Y'
                    else:
                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                        if agent_choice == "Hit":
                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                            for value in agent_draw:
                                if value == 11:
                                    print("Would you like to change this to a 1?")
                                    #Allow agent to choose yes or no then update accordingly
                                    if agent_choice_ace == 'Y':
                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                            if sum(agent_draw) == 21:
                                print("You've hit the max without going over! Let's see what the house has")
                            elif sum(agent_draw) > 21:
                                bust = 'Y'
                            else:
                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                if agent_choice == "Hit":
                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                    for value in agent_draw:
                                        if value == 11:
                                            print("Would you like to change this to a 1?")
                                            #Allow agent to choose yes or no then update accordingly
                                            if agent_choice_ace == 'Y':
                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                    if sum(agent_draw) == 21:
                                        print("You've hit the max without going over! Let's see what the house has")
                                    elif sum(agent_draw) > 21:
                                        bust = 'Y'
                                    else:
                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                        if agent_choice == "Hit":
                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                            for value in agent_draw:
                                                if value == 11:
                                                    print("Would you like to change this to a 1?")
                                                    #Allow agent to choose yes or no then update accordingly
                                                    if agent_choice_ace == 'Y':
                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                            if sum(agent_draw) == 21:
                                                print("You've hit the max without going over! Let's see what the house has")
                                            elif sum(agent_draw) > 21:
                                                bust = 'Y'
                                            else:
                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                if agent_choice == "Hit":
                                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                    for value in agent_draw:
                                                        if value == 11:
                                                            print("Would you like to change this to a 1?")
                                                            #Allow agent to choose yes or no then update accordingly
                                                            if agent_choice_ace == 'Y':
                                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                    if sum(agent_draw) == 21:
                                                        print("You've hit the max without going over! Let's see what the house has")
                                                    elif sum(agent_draw) > 21:
                                                        bust = 'Y'
                                                    else:
                                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                        if agent_choice == "Hit":
                                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                            for value in agent_draw:
                                                                if value == 11:
                                                                    print("Would you like to change this to a 1?")
                                                                    #Allow agent to choose yes or no then update accordingly
                                                                    if agent_choice_ace == 'Y':
                                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                            if sum(agent_draw) == 21:
                                                                print("You've hit the max without going over! Let's see what the house has")
                                                            elif sum(agent_draw) > 21:
                                                                bust = 'Y'
                                                            else:
                                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                if agent_choice == "Hit":
                                                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                    for value in agent_draw:
                                                                        if value == 11:
                                                                            print("Would you like to change this to a 1?")
                                                                            #Allow agent to choose yes or no then update accordingly
                                                                            if agent_choice_ace == 'Y':
                                                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                    if sum(agent_draw) == 21:
                                                                        print("You've hit the max without going over! Let's see what the house has")
                                                                    elif sum(agent_draw) > 21:
                                                                        bust = 'Y'
                                                                    else:
                                                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                        if agent_choice == "Hit":
                                                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                            for value in agent_draw:
                                                                                if value == 11:
                                                                                    print("Would you like to change this to a 1?")
                                                                                    #Allow agent to choose yes or no then update accordingly
                                                                                    if agent_choice_ace == 'Y':
                                                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                            if sum(agent_draw) == 21:
                                                                                print("You've hit the max without going over! Let's see what the house has")
                                                                            elif sum(agent_draw) > 21:
                                                                                bust = 'Y'
                                                                            else:
                                                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                if agent_choice == "Hit":
                                                                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                    for value in agent_draw:
                                                                                        if value == 11:
                                                                                            print("Would you like to change this to a 1?")
                                                                                            #Allow agent to choose yes or no then update accordingly
                                                                                            if agent_choice_ace == 'Y':
                                                                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                    if sum(agent_draw) == 21:
                                                                                        print("You've hit the max without going over! Let's see what the house has")
                                                                                    elif sum(agent_draw) > 21:
                                                                                        bust = 'Y'
                                                                                    else:
                                                                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                        if agent_choice == "Hit":
                                                                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                            for value in agent_draw:
                                                                                                if value == 11:
                                                                                                    print("Would you like to change this to a 1?")
                                                                                                    #Allow agent to choose yes or no then update accordingly
                                                                                                    if agent_choice_ace == 'Y':
                                                                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                            if sum(agent_draw) == 21:
                                                                                                print("You've hit the max without going over! Let's see what the house has")
                                                                                            elif sum(agent_draw) > 21:
                                                                                                bust = 'Y'
                                                                                            else:
                                                                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                                if agent_choice == "Hit":
                                                                                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                                    for value in agent_draw:
                                                                                                        if value == 11:
                                                                                                            print("Would you like to change this to a 1?")
                                                                                                            #Allow agent to choose yes or no then update accordingly
                                                                                                            if agent_choice_ace == 'Y':
                                                                                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                                    if sum(agent_draw) == 21:
                                                                                                        print("You've hit the max without going over! Let's see what the house has")
                                                                                                    elif sum(agent_draw) > 21:
                                                                                                        bust = 'Y'
                                                                                                    else:
                                                                                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                                        if agent_choice == "Hit":
                                                                                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                                            for value in agent_draw:
                                                                                                                if value == 11:
                                                                                                                    print("Would you like to change this to a 1?")
                                                                                                                    #Allow agent to choose yes or no then update accordingly
                                                                                                                    if agent_choice_ace == 'Y':
                                                                                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                                            if sum(agent_draw) == 21:
                                                                                                                print("You've hit the max without going over! Let's see what the house has")
                                                                                                            elif sum(agent_draw) > 21:
                                                                                                                bust = 'Y'
                                                                                                            else:
                                                                                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                                                if agent_choice == "Hit":
                                                                                                                    agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                                                    for value in agent_draw:
                                                                                                                        if value == 11:
                                                                                                                            print("Would you like to change this to a 1?")
                                                                                                                            #Allow agent to choose yes or no then update accordingly
                                                                                                                            if agent_choice_ace == 'Y':
                                                                                                                                agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                                                    if sum(agent_draw) == 21:
                                                                                                                        print("You've hit the max without going over! Let's see what the house has")
                                                                                                                    elif sum(agent_draw) > 21:
                                                                                                                        bust = 'Y'
                                                                                                                    else:
                                                                                                                        print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                                                                                                                        if agent_choice == "Hit":
                                                                                                                            agent_draw.append(deck.pop(random.randrange(0,len(deck))))
                                                                                                                            for value in agent_draw:
                                                                                                                                if value == 11:
                                                                                                                                    print("Would you like to change this to a 1?")
                                                                                                                                    #Allow agent to choose yes or no then update accordingly
                                                                                                                                    if agent_choice_ace == 'Y':
                                                                                                                                        agent_draw = [1 if i == 11 else i for i in agent_draw]
                                                                                                                            if sum(agent_draw) == 21:
                                                                                                                                print("You've hit the max without going over! Let's see what the house has")
                                                                                                                            elif sum(agent_draw) > 21:
                                                                                                                                bust = 'Y'
                                                                                                                            else:
                                                                                                                                print("Current hand value: "+str(sum(agent_draw))+" Would you like to Hit or Stay?")
                    
    #STOP GAME AGENT CHOICE LOGIC
    
    #house rules state that dealer must draw until they reach at least 17. if 17 is reached they must stay
    if blackjack_status == 'N' and bust = 'N':
        while sum(house_draw) < 17:
            house_draw.append(deck.pop(random.randrange(0,len(deck))))
            if sum(house_draw) > 21:
                #Currently, updating all aces in hand to 1. NEED TO DETERMINE A WAY TO ONLY UPDATE LATEST DRAW
                house_draw = [1 if i == 11 else i for i in house_draw]
    
    print(sum(agent_draw))
    
    #START GAME REWARD LOGIC
    if bust = 'Y':
        print("bust! you lose this round")
        bank = bank-bet
        losses = losses+1
    elif sum(house_draw) == 21 and sum(agent_draw) == 21:
        print("Push, you get your original bet back")
    elif sum(house_draw) == 21 and sum(agent_draw) != 21:
        print("you lose this round")
        bank = bank-bet
        losses = losses+1
    elif sum(house_draw) != 21 and sum(agent_draw) == 21:
        print("Blackjack! You win!")
        bank = bank+(bet*2)
        wins = wins +1
    elif sum(agent_draw) > 21:
        print("bust! You lose this round")
        bank = bank-bet
        losses = losses+1
    elif sum(house_draw) == sum(agent_draw):
        print("Push, you get your original bet back")
    elif sum(house_draw) < sum(agent_draw):
        print("you win!")
        bank = bank+bet
        wins = wins +1
    elif sum(house_draw) < 21 and sum(house_draw) > sum(agent_draw):
        print("you lose")
        bank = bank-bet
        losses = losses+1
    elif sum(house_draw) > 21 and sum(agent_draw) < 21:
        print("you win!")
        bank = bank+bet
        wins = wins +1
    #END GAME REWARD LOGIC
        
    print(sum(deck))
    #if sum(deck) < 60:
        #re-create deck
    #    deck = initdeck.deck()

    
    gameCounter += 1
    print("current bank amount: $"+str(bank))
    print("Continue Playing?")
    AgentContinue = 'Y'
    
    #End While Loop

if AgentContinue = 'N'
    print("You have chosen not to continue playing")
    print("total games played: ",str(gameCounter))
    print(f"total wins so far: {wins}")
    print(f"Perecentage wins: {(wins/gameCounter) * 100}%")

if bank < 1.00:
    print("Game Over, no money left in the bank")
    print("total games played: ",str(gameCounter))
    #AI cannot continue if bank < minimum bet

if sum(deck) < 60:
    print('Re-shuffling deck')
    print('current bank value: '+str(bank))
    print("total games played so far: ",str(gameCounter))
    print(f"total wins so far: {wins}")
    print(f"Perecentage wins: {(wins/gameCounter) * 100}%")
    #call "deck" class to re-instantiate the deck