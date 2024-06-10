import random
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = 'X'
winner = None
gameRunning = True


#printing the game board
def printBoard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}\n'
          f'----------\n'
          f'{board[3]} | {board[4]} | {board[5]}\n'
          f'----------\n'
          f'{board[6]} | {board[7]} | {board[8]}\n')

#take player input
def playerInput(board):
    validAnswer = False
    while validAnswer == False:
        choice = int(input('Choose a number 1-9: '))
        if choice >= 1 and choice <= 9 and board[choice - 1] == '-':
            board[choice - 1] = currentPlayer
            validAnswer = True
        else:
            print('Input Error! Number is either not within range or spot has been claimed already.')

#check for win or tie
def WinCondition(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = currentPlayer
        return True
    if board[3] == board[4] == board[5] and board[3] != '-':
        winner = currentPlayer
        return True
    if board[6] == board[7] == board[8] and board[6] != '-':
        winner = currentPlayer
        return True
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = currentPlayer
        return True
    if board[1] == board[4] == board[7] and board[1] != '-':
        winner = currentPlayer
        return True
    if board[2] == board[5] == board[8] and board[2] != '-':
        winner = currentPlayer
        return True
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = currentPlayer
        return True
    if board[2] == board[4] == board[6] and board[2] != '-':
        winner = currentPlayer
        return True

def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print("Tie")
        gameRunning = False

def checkWin():
    global gameRunning
    global board
    if WinCondition(board) == True:
        printBoard(board)
        print(f'Winner: {winner}')
        gameRunning = False

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

#computer player
def botOption():
    choice = input('Type \"1\" if you would like to face a bot and enter anything else if otherwise: ')
    if choice == '1':
        return True

def computerPlayer(board):
    global currentPlayer
    validAnswer = False
    while validAnswer == False:
        choice = random.randint(0, 8)
        if board[choice] == '-':
            board[choice] = '0'
            validAnswer = True

#check for win or tie again
botOrNot = botOption()
while gameRunning:
    printBoard(board)
    if currentPlayer == 'X' or currentPlayer == 'O' and botOrNot != True:
        playerInput(board)
    if currentPlayer == 'O' and botOrNot == True:
        print('Bot\'s move')
        computerPlayer(board)
    checkWin()
    checkTie(board)
    switchPlayer()