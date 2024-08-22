def play_game(board,boardSize):
    
    #Starting Player
    player = "X"
    #Checks if every tile has been played if so move on
    while not isGameOver(board):
    
        #Checks player answer is a correct co-ordinate
        row, column = validAnswer(player,board)
        
        #Updates board to reflect move
        board, player = makeMove(board, row, column, player)

    print(printBoard(board))
    #Calculates who had the most amount of 3 lines
    whoWon(board,boardSize)
    print("Game over!")


#Reads board to player in readable format
def printBoard(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid

#Changes board to reflect player action
def makeMove(board, row, column, player):

    #Checks if a move has already been played, if so keep conditions the same
    if board[row][column] in ['X','O']:
        print('please play a valid move')
        return (board, player)
    else:
        
        #Swaps player and updates board value
        board[row][column] = player
        if player == 'O':
            player = 'X'
        else:
            player = 'O'
    return (board, player)

#Just checks all values in board until a null value hit, the game isnt over if so
def isGameOver(board):
    for row in board:
        for value in row:
            if value == '.':
                return False
    return True

#Calculates final scores
def whoWon(board,boardSize):
    #Checks each co-ordinate, calculates if any lines form from it and moves on
    letterTally=[]
    for rowCount in range(boardSize):
        for columnCount in range(boardSize):
            #down
            if rowCount + 2 <=boardSize-1:
                letter1 = board[rowCount][columnCount]
                letter2 = board[rowCount+1][columnCount]
                letter3 = board[rowCount+2][columnCount]
                letterTally.append(checkLetter(letter1, letter2, letter3))

                #diagLeft
                if columnCount-2>=0:
                    letter1 = board[rowCount][columnCount]
                    letter2 = board[rowCount+1][columnCount-1]
                    letter3 = board[rowCount+2][columnCount-2]
                    letterTally.append(checkLetter(letter1, letter2, letter3))
            #right
            if columnCount+2<=boardSize-1:
                letter1 = board[rowCount][columnCount]
                letter2 = board[rowCount][columnCount+1]
                letter3 = board[rowCount][columnCount+2]
                letterTally.append(checkLetter(letter1, letter2, letter3))
            
                #diagRight
                if rowCount+2<=boardSize-1:
                    letter1 = board[rowCount][columnCount]
                    letter2 = board[rowCount+1][columnCount+1]
                    letter3 = board[rowCount+2][columnCount+2]
                    letterTally.append(checkLetter(letter1, letter2, letter3))
    #Now we tally the results from letterTally, more letters means higher score.
    xScore = 0
    oScore = 0
    for letterTracker in letterTally:
        if letterTracker == 'X':
            xScore +=1
        elif letterTracker =='O':
            oScore +=1
    #Final print so players know who won
    if xScore > oScore:
        print(f'And X is the winner with {xScore} points! O coming close second with {oScore} points')
    elif xScore == oScore:
        print(f'And we have a tie at {xScore} points!')
    else:
        print(f'And O is the winner with {oScore} points! X coming close second with {xScore} points')

#Constructs the board from boardSize (also weird ass feature),
#You cant build the row outside the for loop or it links them and copies the values between them
def buildBoard(boardSize):
    board = []
    for _ in range(boardSize):
        row = ["."] * boardSize  
        board.append(row)  
    return board

#Checks if a 3 link has been found, if so return the player who has the link
def checkLetter(letter1, letter2, letter3):
    if letter1 == letter2 and letter2 == letter3:
        return letter1
    else:
        return False

#Main interface, ensures correct valuies go through and converts rows (row 1, into row 0 for code logic)
def validAnswer(player,board):
    while True:
        print(printBoard(board))
        print("It's " + player + "'s turn.")
        row = input("Enter a row [>]: ") 
        column = input("Enter a column [^]: ")
        try:
            row = int(row)-1
            column = int(column)-1
            if row<0 or row>boardSize-1:
                print(f'Input a correct row between 1-{boardSize}')
            else:
                if column<0 or column>boardSize-1:
                    print(f'Input a correct column between 1-{boardSize}')
                else:            
                    return row, column
        except:
            print("Please input an integer")

#Start of Code! Gets correct value for boardSize and we build the board to play!
print("Game time!")
while True:
    try:
        boardSize = int(input("What size would you like the board to be?"))
        if boardSize >=3:
            break
        else:
            print("Please input a value higher than 2")
    except:
        print("Please input an integer")
        

board = buildBoard(boardSize)

play_game(board,boardSize)
