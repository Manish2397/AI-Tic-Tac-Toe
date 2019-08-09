import random
import sys

def drawBoard(board):
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def inputPlayerLetter():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter =input().upper()

    
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    
    print('Want to Play again??(yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    if isSpaceFree(board,move):
        board[move] = letter
    else:
        raise Exception("makeMove: the field is not empty!")

def isWinner(board, le):
    
    return ((board[7] == le and board[8] == le and board[9] == le) or (board[4] == le and board[5] == le and board[6] == le) or (board[1] == le and board[2] == le and board[3] == le) or(board[7] == le and board[4] == le and board[1] == le) or (board[8] == le and board[5] == le and board[2] == le) or  (board[9] == le and board[6] == le and board[3] == le) or (board[7] == le and board[5] == le and board[3] == le) or (board[9] == le and board[5] == le and board[1] == le)) 

def getBoardCopy(board):
    
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
   
    return board[move].isdigit()

def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move =input()
    return int(move)

def chooseRandomMove(board, movesList):
    
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) > 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

   
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    
    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

 
    if isSpaceFree(board, 5):
        return 5

   
    return chooseRandomMove(board, [2, 4, 6, 8])

def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def main():
    print('Welcome to Tic Tac Toe!')
    random.seed()
    while True:
        # Reset the board
        theBoard = [' '] * 10
        for i in range(9,0,-1):
            theBoard[i] = str(i)
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turn == 'player':
                
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
    
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print("You Won!!!")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
    
            else:
                
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
    
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print("Sorry,You Lose!!")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
    
        if not playAgain():
            break
        
if __name__ == "__main__":
    main()
