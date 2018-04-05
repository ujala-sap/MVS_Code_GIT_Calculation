# This is a tic tac toe game
from IPython.display import clear_output
import random

# Define the user details
def user_details():
    Player1 = input('Enter Your Name : Player 1 : ')
    Player2 = input('Enter Your Name : Player 2 : ')
    print('Welcome {} and {} in the game'.format(Player1, Player2))
    print('Lest Start the Game')

# Create a board to play the game
def display_board(board_list):
    clear_output() # Clear the board

    print('   |   |   ')
    print(' '+board_list[7]+' | '+board_list[8]+' | '+board_list[9])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' '+board_list[4]+' | '+board_list[5]+' | '+board_list[6])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' '+board_list[1]+' | '+board_list[2]+' | '+board_list[3])
    print('   |   |   ')

user_details()