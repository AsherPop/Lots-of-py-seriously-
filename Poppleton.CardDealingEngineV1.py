"""
Card Dealing Engine


Questions from previous class:
1. How do you represent each card?
2. A card displays three pieces of data...which ones do you need?  Which is the only piece of data that is IMPLIED by another piece?
3. How do you organize the deck, player "hands", and a discard "pile"?
4. How do you represent relative VALUE between cards?
5. How can you simulate shuffling?
6. How do you "deal"?

This document is going to be where we work on our Card Dealing Engine.
Below I'm going to be leaving you some instructions or asking questions in RED
"""

#The instructions and questions look like this

"""
So make sure that you pay attention as much as you can to the rules of
Python syntax in order to prevent errors.

Try to directly address each question above and if you need to,
you can put your pseudo code in multi-line comments like these
by using triple quotation marks
"""


#What library do you import to be able to make random selections?
import random

#Put your data structure here that represents a card deck.  I'd suggest a list

#Should your player hands be lists too? Where is a good place to write those?

playerHand = []
cardDeck = []

def cardEngine
    while True:
        playerNumber = input("How many people are playing?     ")
        dealNumber = input("How many cards would you like to draw?     ")
        cardDeck = list(random.randint(range(1,14), ["Spade", "Club", "Diamond", "Heart"])
        random.shuffle(cardDeck)
        
        for x in range(0, int(dealNumber)):
                        playerHand.append(random.randint(0, int(playerNumber)))
            
            #for card in carddeck
                #append random card type to player hand
        for x in range(0, int(dealNumber)):
                        playerHand.append(random.randint(0, cardDeck))
                       
                       
                                    
        
        print("Here are your cards: {}".format(playerHand))
        #find way to print values in hand with random values of suits

        





#Here's where your program starts.  What kind of loop should you use?
#Think about creating variables and assigning them input() values
#For example: dealNumber = input("How many cards should I deal?   ")


#How will you randomize the deck (like shuffling)? Do that inside your loop
#Start with a set number of cards (like two) that you deal to each "player"
#How do you represent the hands for each player?










