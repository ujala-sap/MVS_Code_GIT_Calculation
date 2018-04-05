'''
DOCSTRING : This is a Tic Tac Toe Game Python Program
'''
# Below are the requirements
# 1. 2 players should be able to play the game (both sitting at the same computer)
# 2. The board should be printed out every time a player makes a move
# 3. You should be able to accept input of the player position and then place a symbol on the board

# Create a board to play the game
from IPython.display import clear_output
import random

Player1 = input('Enter Your Name : Player 1 : ')
Player2 = input('Enter Your Name : Player 2 : ')
print('Welcome {} and {} in the game'.format(Player1, Player2))
print('Lest Start the Game')

def display_board(board):
    clear_output() #This will clear the board to play a fresh game

    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

# Player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("{} : Do you want to be 'X' or 'O' ? ".format(Player1)).upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place marker in the board
def place_marker(board, marker, position):
    board[position] = marker

# Checks for all the possible combination for own the game
def win_check(board, mark):
    return (
        (board[7] == mark and board[4] == mark and board[1] == mark) or # Vertical Left 
        (board[8] == mark and board[5] == mark and board[2] == mark) or # Vertical Middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # Vertical Right
        (board[1] == mark and board[2] == mark and board[3] == mark) or # Horizontal Bottom
        (board[4] == mark and board[5] == mark and board[6] == mark) or # Horizontal Middle
        (board[7] == mark and board[8] == mark and board[9] == mark) or # Horizontal Top
        (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
        (board[3] == mark and board[5] == mark and board[7] == mark)    # Diagonal
    )

# Function to randomly decide which player will go first
def choose_first():
    if random.randint(0,1) == 0:
        return Player2
    else:
        return Player1

# Write a function to check whether a space in the board is available or not, returns a boolean value
def space_check(board, position):
    return board[position] == ' '

# Write a function to check if boardos full or space available
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Function to ask the user for a next position and then check if the position is free and 
# if it is free then return the positio for later use
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position : (1-9) '))
    
    return position

# Function to ask the user if they want to play again and return the boolean True if they wants to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Login to run the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the Board
    theBoard = [' '] * 10
    # Set the player marker
    player1_marker , player2_marker = player_input()
    # Set the User truns
    turn = choose_first()

    print(turn + ' will go first')

    play_game = input('Are you ready to play the game ? Enter Yes or No. ')

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == Player1:
            # Player 1 turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! {}.. You have won the game!'.format(Player1))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a Draw')
                    break
                else:
                    turn = Player2

        else:
            #Player 2 Turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('{} has own the game'.format(Player2))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = Player1
    if not replay():
        break
