import random


#NOTES FROM THE DO NOW:
#1. Work with integers
#2. Random number generator
#3. Way to give commands

#FEATURES TO ADD:
#how to keep program running until I quit
#Show multiple rolls with numberOfRolls
#Add roll totalling features(sum/highest/lowest)
#More human interface

myRolls = []


#a while loop will run forever until it's deliberately exited
def diceEngine():
    while True:
        dieType = input("How many sides should the die have?        ")
        numberOfRolls = input("How many times would you like to roll?      ")
        rollTotal = 0


        #use for loop to repeat through the number of rolls


        for x in range(0, int(numberOfRolls)):
            myRolls.append(random.randint(1, int(dieType)))


        print("Here are your rolls: {}".format(myRolls))
        print("Your roll total was: {}".format(sum(myRolls)))
        print("Your highest roll was: {}".format(max(myRolls)))
        print("Your lowest roll was: {}".format(min(myRolls)))

        #add a way to exit the loop
        rollAgain = input("Would you like to roll again? yes or no?       ")
        if rollAgain == "no":
            break
        #add a way to clear the list for next roll

        clearList = input("Do you want me to clear your list of rolls? yes or no     ")
        if clearList == "yes":
            myRolls.clear()

if __name__ == "__main__":
    diceEngine()




