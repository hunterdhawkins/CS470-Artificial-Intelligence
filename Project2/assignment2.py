import copy
import random
import numpy as np
rows = 6
cols = 7
maxdepth = 6
alpha = -9999
beta = 9999


board = [[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]]

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



#Only recognizes win or loss
#Our AI cannot win, it only defends
#Give AI random move if all evaluate to the same
def printB(b):
    for r in b:
        for v in r:
            print("|", end= "")
            print( v, end= "|")
        print()
    print()

#check for wins and try to do some evaluations
def checkWinOrEval(b):
    score =0
    #Horizontal, left to right
    for i in range(rows):
        for j in range(cols-3):
            if(b[i][j] == 'X' and b[i][j+1] == 'X' and b[i][j+2] == 'X' and b[i][j+3] == 'X'):
                score = 1
                return score #AI 1 win
            if(b[i][j] == 'T' and b[i][j+1] == 'T' and b[i][j+2] == 'T' and b[i][j+3] == 'T'):
                score = -1
                return score #Player win/ AI #2 win
            if (b[i][j] == 'X' and b[i][j + 1] == 'X' and b[i][j+2] == 'X' and b[i][j+3] == 0):
                score = 0.5
                return score
            if (b[i][j] == 'T' and b[i][j+1] == 'T' and b[i][j+2] == 'T' and b[i][j+3] == 0):
                score -0.5
                return score
            if (b[i][j] == 'X' and b[i][j + 1] == 'X' and b[i][j+2] == 0 and b[i][j+3] == 0):
                score = 0.2
                return score
            if (b[i][j] == 'T' and b[i][j+1] == 'T' and b[i][j+2] == 0 and b[i][j+3] == 0):
                score = 0.2
                return score
    #horizontal, right to left
    for i in reversed(range(rows)):
        for j in range(cols - 3):
            if (b[i][j] == 'X' and b[i][j - 1] == 'X' and b[i][j - 2] == 'X' and b[i][j - 3] == 'X'):
                score = 1
                return score  # AI 1 win
            if (b[i][j] == 'T' and b[i][j - 1] == 'T' and b[i][j - 2] == 'T' and b[i][j - 3] == 'T'):
                score = -1
                return score  # Player win/ AI #2 win
            if (b[i][j] == 'X' and b[i][j - 1] == 'X' and b[i][j - 2] == 'X' and b[i][j - 3] == 0):
                score = 0.5
                return score
            if (b[i][j] == 'T' and b[i][j - 1] == 'T' and b[i][j - 2] == 'T' and b[i][j - 3] == 0):
                score - 0.5
                return score
            if (b[i][j] == 'X' and b[i][j - 1] == 'X' and b[i][j - 2] == 0 and b[i][j - 3] == 0):
                score = 0.2
                return score
            if (b[i][j] == 'T' and b[i][j - 1] == 'T' and b[i][j - 2] == 0 and b[i][j - 3] == 0):
                score = 0.2
                return score
    #Vertical
    for i in range(rows-3):
        for j in range(cols):
            if (b[i][j] == 'X' and b[i+1][j] == 'X' and b[i+2][j] == 'X' and b[i+3][j] == 'X'):
                score = 1
                return score  # AI 1 win
            if (b[i][j] == 'T' and b[i+1][j] == 'T' and b[i+2][j] == 'T' and b[i+3][j] == 'T'):
                score = -1
                return score  # Player win/ AI #2 win
            if (b[i][j] == 'X' and b[i+1][j] == 'X' and b[i+2][j] == 'X' and b[i+3][j] == 0):
                score = 0.5
                return score
            if (b[i][j] == 'T' and b[i+1][j] == 'T' and b[i+2][j] == 'T' and b[i+3][j] == 0):
                score - 0.5
                return score
            if (b[i][j] == 'X' and b[i+1][j] == 'X' and b[i+2][j] == 0 and b[i+3][j] == 0):
                score = 0.2
                return score
            if (b[i][j] == 'T' and b[i+1][j] == 'T' and b[i+2][j] == 0 and b[i+3][j] == 0):
                score = 0.2
                return score

    #Diagonal
    for i in range(rows - 3):
        for j in range(3,cols):
            if (b[i][j] == 'X' and b[i + 1][j-1] == 'X' and b[i + 2][j-2] == 'X' and b[i + 3][j-3] == 'X'):
                    score = 1
                    return score  # AI 1 win
            if (b[i][j] == 'T' and b[i + 1][j-1] == 'T' and b[i + 2][j-2] == 'T' and b[i + 3][j-3] == 'T'):
                    score = -1
                    return score  # Player win/ AI #2 win
            if (b[i][j] == 'X' and b[i + 1][j-1] == 'X' and b[i + 2][j-2] == 'X' and b[i + 3][j-3] == 0):
                    score = 0.5
                    return score
            if (b[i][j] == 'T' and b[i + 1][j-1] == 'T' and b[i + 2][j-2] == 'T' and b[i + 3][j-3] == 0):
                    score - 0.5
                    return score
            if (b[i][j] == 'X' and b[i + 1][j-1] == 'X' and b[i + 2][j-2] == 0 and b[i + 3][j-3] == 0):
                    score = 0.2
                    return score
            if (b[i][j] == 'T' and b[i + 1][j-1] == 'T' and b[i + 2][j-2] == 0 and b[i + 3][j-3] == 0):
                    score = 0.2
                    return score

    #Diagonal #2
    for i in range(3,rows):
        for j in range(3, cols):
            if (b[i][j] == 'X' and b[i -1][j-1] == 'X' and b[i - 2][j-2] == 'X' and b[i - 3][j-3] == 'X'):
                    score = 1
                    return score  # AI 1 win
            if (b[i][j] == 'T' and b[i - 1][j-1] == 'T' and b[i - 2][j-2] == 'T' and b[i - 3][j-3] == 'T'):
                    score = -1
                    return score  # Player win/ AI #2 win
            if (b[i][j] == 'X' and b[i - 1][j-1] == 'X' and b[i - 2][j-2] == 'X' and b[i - 3][j-3] == 0):
                    score = 0.5
                    return score
            if (b[i][j] == 'T' and b[i - 1][j-1] == 'T' and b[i - 2][j-2] == 'T' and b[i - 3][j-3] == 0):
                    score - 0.5
                    return score
            if (b[i][j] == 'X' and b[i - 1][j-1] == 'X' and b[i - 2][j-2] == 0 and b[i - 3][j-3] == 0):
                    score = 0.2
                    return score
            if (b[i][j] == 'T' and b[i - 1][j-1] == 'T' and b[i - 2][j-2] == 0 and b[i - 3][j-3] == 0):
                    score = 0.2
                    return score

    return score

def move(char):
    m = None
    while (m == None or m >= cols or m < 0 or board[0][m] !=0):
        m = int(input("Move: "))
    makeMove(board, m, char)


def makeMove(b, col, char):
    for r in range(5,-1,-1):
        if(b[r][col] == 0):
            b[r][col] = char
            return


#Return the best column to place the chip in
def chooseMove(b):
    bestmove = None
    bestvalue = float("-inf")
    tempValues = []
    for c in range(0, cols):
        if(b[0][c] == 0):   #0 is top row, make sure column is not full
            value = mini(b,c,1) #b = current board, c = column for move, 1 is the depth
            tempValues.insert(0, value)
            print(str(c) + " value= " + str(value))
            if(value > bestvalue): #If the current value is better then the best prior value assign it
                bestvalue = value
                bestmove = c
            if all ([v == 0 for v in tempValues]): #If all the AI calculations come out to zero
                bestmove = random.randint(0,6) #Choose random column to place in
    return bestmove

#find minimum value but if no win or loss call maxi function
def mini(b, c, depth):
    global beta
    global alpha
    newb = copy.deepcopy(b) #make temporary new board to look ahead
    makeMove(newb, c, 'X') #Place AI piece
    s = checkWinOrEval(newb)
    #s = score_move(newb, 'X')
    if(s == 1):
        return s #winner
    if(s == -1):
        return s #winner
    if(depth == maxdepth):
        return s #currently always 0
    worstvalue = float("inf")
    for c in range (0,cols):
        if(b[0][c] == 0): #Make sure column is empty
            value = maxi(newb,c,depth+1)
            if(value < worstvalue):
                worstvalue = value
            beta = min(beta,value) #alpha beta pruning
            if beta <= alpha:
                break
    return worstvalue

def maxi(b, c, depth):
    global beta
    global alpha
    newb = copy.deepcopy(b) #make temporary new board to look ahead
    makeMove(newb, c, 'T') #Place player piece
    s = checkWinOrEval(newb)
    #s = score_move(newb, 'X')
    if(s == 1):
        return s # AI wins
    if(s == -1):
        return s # player wins
    if(depth == maxdepth):
        return s #currently always 0
    bestvalue = float("-inf")
    for c in range (0,cols):
        if(b[0][c] == 0): #Make sure column is empty
            value = mini(newb,c,depth+1)
            if(value > bestvalue):
                bestvalue = value
            alpha = max(alpha, value) #alpha beta pruning
            if beta <= alpha:
                break
    return bestvalue

def PlayervsAi(userin):
    game_over = False
    while not game_over:
        if (userin == 1):
            print("The AI is planning its move")
            mv = chooseMove(board)
            makeMove(board, mv, 'X')
            printB(board)
            if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
                game_over = True
                if (checkWinOrEval(board) == 1):
                    print(color.RED +"AI wins")
                else:
                    print(color.BLUE +"Player wins")

            move('T')  # visually different then zeros in board
            printB(board)
            if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
                game_over = True
                if (checkWinOrEval(board) == 1):
                    print(color.RED +"AI wins")
                else:
                    print(color.BLUE +"Player wins")
        else:
            printB(board)
            move('T')  # visually different then zeros in board
            printB(board)
            if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
                game_over = True
                if (checkWinOrEval(board) == 1):
                    print("AI wins")
                else:
                    print("Player wins")
            mv = chooseMove(board)
            makeMove(board, mv, 'X')
            printB(board)
            if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
                game_over = True
                if (checkWinOrEval(board) == 1):
                    print("AI wins")
                else:
                    print("Player wins")

def AivsAI():
    game_over = False
    while not game_over:
        #AI number one playing
        print("AI #1 is planning its move")
        mv = chooseMove(board)
        makeMove(board, mv, 'X')
        printB(board)
        if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
            game_over = True
            if (checkWinOrEval(board) == 1):
                print(color.RED +"AI #1 wins")
            else:
                print(color.BLUE +"AI #2 wins")
        #AI number two playing
        print("AI #2 is planning its move")
        mv = chooseMove(board)
        makeMove(board, mv, 'T')
        printB(board)
        if (checkWinOrEval(board) == 1 or checkWinOrEval(board) == -1):
            game_over = True
            if (checkWinOrEval(board) == 1):
                print(color.BLUE +"AI #2 wins")
            else:
                print(color.RED +"AI #1 wins")

#Starting here is kinda like int main()
print("Do you want to play or do you want to watch two AI's play")
print("1 = Player vs AI, 2 = AI vs AI")
userin = int(input())
if(userin == 1):
    print("Do you want the AI to go first or the player?")
    print("1 = AI first, 2 = Player first")
    userin2 = int(input())
    PlayervsAi(userin2)
else:
    AivsAI()

