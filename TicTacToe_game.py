# -------------------------------
# TIC TAC TOE GAME (2 Player)
# -------------------------------

# Initialize 3x3 board with empty spaces
r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']

# -------------------------------
# Function to take initial input for player 1
# -------------------------------
def initial_input():
    return input('Player 1: Do you want to be X or O?  ')

# -------------------------------
# Function to validate and assign Player 1 choice
# -------------------------------
def p1input():
    x = False
    while not x:
        p1 = initial_input()
        if p1 not in ['X', 'O']:
            print('Invalid input. Input either X or O  ')
            continue
        elif p1 == 'X':
            print('Player 1 will go first  ')
            x = True
        else:
            print('Player 2 will go first  ')
            x = True

# -------------------------------
# Function to print the Tic-Tac-Toe board
# -------------------------------
def printfunc(r1, r2, r3):
    print('     '+r1[0]+'|'+r1[1]+'|'+r1[2])
    print('-----------------')
    print('     '+r2[0]+'|'+r2[1]+'|'+r2[2])
    print('-----------------')
    print('     '+r3[0]+'|'+r3[1]+'|'+r3[2])
    print('-----------------')

# -------------------------------
# Function to take next move input
# -------------------------------
def furtherinp(lt):
    bol = False
    while not bol:
        st = input('Choose your next position (1-9)  ')
        # Validate input
        if st.isdigit() and st in lt:
            bol = True
        else:
            print('Sorry that is invalid, retry!  ')
    return st

# -------------------------------
# Function to update the board with player’s move
# -------------------------------
def printchance(pc, letter):
    if pc == 1:
        r3[0] = letter
    elif pc == 2:
        r3[1] = letter
    elif pc == 3:
        r3[2] = letter
    elif pc == 4:
        r2[0] = letter
    elif pc == 5:
        r2[1] = letter
    elif pc == 6:
        r2[2] = letter
    elif pc == 7:
        r1[0] = letter
    elif pc == 8:
        r1[1] = letter
    else:
        r1[2] = letter

# -------------------------------
# Function to check winning conditions
# -------------------------------
def wincheck(r1, r2, r3, mark):
    return (
        # Check rows
        (r1[0]==mark and r1[1]==mark and r1[2]==mark) or
        (r2[0]==mark and r2[1]==mark and r2[2]==mark) or
        (r3[0]==mark and r3[1]==mark and r3[2]==mark) or
        # Check columns
        (r1[0]==mark and r2[0]==mark and r3[0]==mark) or
        (r1[1]==mark and r2[1]==mark and r3[1]==mark) or
        (r1[2]==mark and r2[2]==mark and r3[2]==mark) or
        # Check diagonals
        (r1[0]==mark and r2[1]==mark and r3[2]==mark) or
        (r1[2]==mark and r2[1]==mark and r3[0]==mark)
    )

# -------------------------------
# Main Game Function
# -------------------------------
def maingame():
    mylist = ['1','2','3','4','5','6','7','8','9']  # Available positions
    chance = 0
    game_won = False

    while chance < 9:
        play = furtherinp(mylist)       # Ask player for move
        mylist.remove(play)             # Remove chosen position
        pk = int(play)

        # Player 1 (X) moves on even chances
        if chance % 2 == 0:
            printchance(pk, 'X')
            if wincheck(r1, r2, r3, 'X'):
                print('Congratulations! X Wins!  ')
                game_won = True
        else:
            printchance(pk, 'O')
            if wincheck(r1, r2, r3, 'O'):
                print('Congratulations! O Wins!  ')
                game_won = True

        printfunc(r1, r2, r3)
        chance += 1

        if game_won:
            break

# -------------------------------
# Game Loop
# -------------------------------
replay = True

while replay:
    print('Welcome to Tic Tac Toe'  )
    r1 = [' ', ' ', ' ']
    r2 = [' ', ' ', ' ']
    r3 = [' ', ' ', ' ']

    p1input()               # Take player 1's choice
    printfunc(r1, r2, r3)    # Print initial empty board
    maingame()               # Start game

    rec = False
    while not rec:
        rep = input('Do you wanna play again? Y or N?  ')
        if rep == 'Y':
            rec = True
        elif rep == 'N':
            print('See you next time!  ')
            replay = False
            rec = True
        else:
            print('Invalid input, either Y or N?  ')
