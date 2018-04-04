'''
DOCSTRING : This is a Game Guess Challenge
INPUT : User input a random number
OUTPUT : Check if user guess the correct number and the no of attempts
'''
#Guessing Game Challenge
#The Challenge:
#Write a program that picks a random integer from 1 to 100, and has players guess the number.
#  The rules are:
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#       within 10 of the number, return "WARM!"
#       further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is
#       closer to the number than the previous guess return "WARMER!"
#       farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly and 
# how many guesses it took!

# Import the random library
from random import randint

# Create a varible to store the random generated number
RAND_NUM = randint(1, 100)
print(RAND_NUM)

# Create a list to hold the no of user guesses
GUESS_LIST = [0]

# Create the logic
while True:
    # Entre the guess number by user
    GUESS_NUM = int(input("Enter a number to guess : "))

    # Check If the guess number by the user is not in range
    if GUESS_NUM not in range(1, 100):
        print("OUT OF BOUNDS... Please try again")
        continue

    # Check if the guess number matches the randon number
    if GUESS_NUM == RAND_NUM:
        print("Congrates.. you done it... You guess the correct number")
        print("You took {} attempts to guess the number".format(len(GUESS_LIST)-1))
        print(GUESS_LIST)
        break

    GUESS_LIST.append(GUESS_NUM)

    # Check if the user doing the guess 1st time and the their guess possibility
    if GUESS_LIST[-2]:
        if abs(RAND_NUM - GUESS_NUM) < abs(RAND_NUM - GUESS_LIST[-2]):
            print("WARMER")
        else:
            print("COLDER")

    else:
        if abs(RAND_NUM-GUESS_NUM) <= 10:
            print("WARM")
        else:
            print("COLD")
