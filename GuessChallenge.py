#Guessing Game Challenge
#The Challenge:
#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#       within 10 of the number, return "WARM!"
#       further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is
#       closer to the number than the previous guess return "WARMER!"
#       farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

# Import the random library
from random import randint

# Create a varible to store the random generated number
rand_num = randint(1,100)
print(rand_num)

# Create a list to hold the no of user guesses
guess_list = [0]

# Create the logic
while True:
    # Entre the guess number by user
    guess_num = int(input("Enter a number to guess : "))

    # Check If the guess number by the user is not in range
    if guess_num not in range(1,100):
        print("OUT OF BOUNDS... Please try again")
        continue

    # Check if the guess number matches the randon number
    if guess_num == rand_num:
        print("Congrates.. you done it... You guess the correct number")
        print("You took {} attempts to guess the number".format(len(guess_list)-1))
        print(guess_list)
        break

    guess_list.append(guess_num)

    # Check if the user doing the guess 1st time and the their guess possibility
    if guess_list[-2]:
        if abs(rand_num - guess_num) < abs(rand_num - guess_list[-2]):
            print("WARMER")
        else:
            print("COLDER")

    else:
        if abs(rand_num-guess_num) <= 10:
            print("WARM")
        else:
            print("COLD")
