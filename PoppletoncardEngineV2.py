

"""

Add following features to program:

1. Make program run until you tell it to quit
2  Put the dealing algorithm in a function and call it at the bottom of the program
with an if __name__ == '__main__' statement
3  Return any input to the user

"""

import random


def cardEngine():
    while True:


        cardDeck = ['AH',
                    '2H',
                    '3H',
                    '4H',
                    '5H',
                    '6H',
                    '7H',
                    '8H',
                    '9H',
                    '10H',
                    'JH',
                    'QH',
                    'KH',
                    'AD',
                    '2D',
                    '3D',
                    '4D',
                    '5D',
                    '6D',
                    '7D',
                    '8D',
                    '9D',
                    '10D',
                    'JD',
                    'QD',
                    'KD',
                    'AS',
                    '2S',
                    '3S',
                    '4S',
                    '5S',
                    '6S',
                    '7S',
                    '8S',
                    '9S',
                    '10S',
                    'JS',
                    'QS',
                    'KS',
                    'AC',
                    '2C',
                    '3C',
                    '4C',
                    '5C',
                    '6C',
                    '7C',
                    '8C',
                    '9C',
                    '10C',
                    'JC',
                    'QC',
                    'KC']

        player1 = []
        player2 = []

        numberToDeal = input("How many cards would you like me to deal?     ")



        try:
            random.shuffle(cardDeck)
            #what is the problem with this line potentially

            if int(numberToDeal) > 0:
                print("I'll deal {} cards to each player".format(numberToDeal))
                for x in range(0, int(numberToDeal)):
                    player1.append(cardDeck.pop(x))
                    player2.append(cardDeck.pop(x+1))
                print(player1)
                print(player2)

            else:
                print("That's not a good number of cards...")

        except ValueError:
            print("That's not a number of cards!")

        pickAgain = input("Would you like to be dealt cards again? y/n    ")
        if pickAgain == "n":
            break

        clearCards = input("Do you want to clear your hand(s)? y/n     ")
        if clearCards == "y":
            player1.clear()
            player2.clear()
            




if __name__ == '__main__':
    cardEngine()
