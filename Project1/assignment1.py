#**************************************
# Hunter Hawkins Stark
# Comp Sci 470: AI | Dr. Soule
# Project #1
# Algorithms used: Breadth first,Lowest cost, Greedy best first, A* with at least two different heuristics.
# Output: Drawn path on the map, all explored squares, current open list, length of path found, and cost of path
#***************************************
#libraries
import os
import math
import time

#*************************************************************
#Class to store data members and functions
#**********************************************************
class Cell:

    def __init__(self, x, y, tile, goalX, goalY, geometry=1): #constructor
        self.priorCell = None
        self.xCord = x
        self.yCord = y
        self.cellType = tile
        self.cost = 0
        self.goalCost = 0
        self.totalCost = 0
        #Used to give the characters in the map their associated values
        if tile == 'R':
            self.cost = 1
        if tile == 'f':
            self.cost = 2
        if tile == 'F':
            self.cost = 4
        if tile == 'h':
            self.cost = 5
        if tile == 'r':
            self.cost = 7
        if tile == 'M':
            self.cost = 10
        # Impassible terrain
        if tile == 'W':
            self.cost = 999999

        #Euclidean distance
        if geometry == 1:
            self.goalCost = math.sqrt(((goalX - x) ** 2) + ((goalY - y) ** 2))
        #Manhatten distance
        if geometry == 2:
            self.goalCost = (abs(goalX - x) + abs(goalY - y))
        #Minkowski distance
        else:
            self.goalCost = (math.ceil((abs(x-goalX)**lam + abs(y-goalY)**lam)**(1/lam)))

        self.totalCost = self.cost + self.goalCost #total cost of path

    def printSelf(self):
        print(self.cellType, end='') #Used to print individual cell value

#**************************************************
#Global variables and lists
#***********************************************
n = 50 #maximum size of the board
cellList = [[0] * n for i in range(n)]
openList = []
closedList = []
printedOpenList =[]
printedClosedList = []

currX = 0
currY = 0

row = 1
column = 1
startRow = 1
startCol = 1
endRow = 1
endCol = 1
solutionFound = 0
openListCounter = 0
searchAlgorithm = 1
geo = 1  #Geometry to be used
lam = 1; #lambda value used in calculating Minkowski distance
#*********************************************
#Function used to print out the final results
#***********************************************
def print_results():
    print('Total cost to goal:', end='')
    print(totalCost)
    print('Total steps taken to goal:', end='')
    print(totalSteps)
    print('Total number of times that cells were added to the open list:', end='')
    print(openListCounter)

#*******************************************************
# Function used to provide initial information to user
#***********************************************************
def initPrompt():
    print("The start is represented by S and the end is represented by G")
    print('This program is used to give a visual representation of search algorithms')
    print('The ◙ symbol represents the open list')
    print ('The ☼ symbol represents the closed list')
    print('The path found by the algorithm is represented by ☺')

#********************************************************************
#Function used to search cells and add them to open list/ closed list
#*********************************************************************
def search(cells, open, closed, endRow, endCol):
    global solutionFound
    global searchAlgorithm
    global openListCounter
    success = 0
    tile = open.pop(0) # put first element onto open list
    if tile not in closed: #if our tile is not in the closed list
        closed.append(tile) #append first element in the open list (starting point) to the closed list
        success = 1 #successfu lIteration so start again until found solution
        tile.cellType = '☼'
        if (tile.xCord == endRow and tile.yCord == endCol): #if our current tile is equal to end x and y value
            solutionFound = 1
            return success
    else:
        return success

    #Logic for the below neighbor
    neighbor = cells[tile.xCord][tile.yCord - 1]
    if neighbor:
        if neighbor not in closed and neighbor.cellType != 'W' and neighbor not in open:
            openListCounter += 1
            neighbor.priorCell = tile
            neighbor.cellType = '◙'
            success = 1
            open.insert(0, neighbor)
    #Logic for the neighbor above
    neighbor = cells[tile.xCord][tile.yCord + 1]
    if neighbor:
        if neighbor not in closed and neighbor.cellType != 'W' and neighbor not in open:
            openListCounter += 1
            neighbor.priorCell = tile
            neighbor.cellType = '◙'
            success = 1
            open.insert(0, neighbor)

    #logic for the neighbor to the left
    neighbor = cells[tile.xCord - 1][tile.yCord]
    if neighbor:
        if neighbor not in closed and neighbor.cellType != 'W' and neighbor not in open:
            openListCounter += 1 #Increment the total cells added to the open list
            neighbor.priorCell = tile
            neighbor.cellType = '◙'
            success = 1
            open.insert(0, neighbor)

    #logic for the neighbor to the right
    neighbor = cells[tile.xCord + 1][tile.yCord]
    if neighbor:
        if neighbor not in closed and neighbor.cellType != 'W' and neighbor not in open:
            openListCounter += 1
            neighbor.priorCell = tile
            neighbor.cellType = '◙'
            success = 1
            open.append(neighbor)

    return success

#***************************************************
# Starting the program
# Reading in the file
# Running the search algorithm
# Print out the results
#**********************************************************
initPrompt()
print('Please enter a number for the type of algorithm to use.')
print('1 = breadth first. 2 = lowest cost. 3 = greedy best first. 4 = A*')
searchAlgorithm = int(input())

if searchAlgorithm == 3 or searchAlgorithm == 4:
    print('1 = Euclidean. 2 = Manhattan 3 = Minkowski')
    geo = int(input())
    if geo == 3:
        print('What do you want your lambda value to be')
        lam = int (input())

#start reading in the file
f = open("input.txt", "r")
for line in f:
    if endCol == 1:
        for word in line.split():
            if row == 1:
                row = int(word)
                continue
            if column == 1:
                column = int(word)
                continue
            if startRow == 1:
                startRow = int(word)
                continue
            if startCol == 1:
                startCol = int(word)
                continue
            if endRow == 1:
                endRow = int(word)
                continue
            if endCol == 1:
                endCol = int(word)
                break
    else:
        for ch in line:
            if ch.strip():
                cellList[currX][currY] = Cell(currX, currY, ch, int(endRow), int(endCol), geo)
                currX += 1
        currX = 0
        currY += 1

openList.append(cellList[startRow][startCol])   #append first cell onto the open list

while openList and not solutionFound: #while there is still items in the open list and we havent found a solution
    if search(cellList, openList, closedList, endRow, endCol):
        if searchAlgorithm == 2:
            openList.sort(key=lambda z: (z.cost)) #Lowest cost
        if searchAlgorithm == 3:
            openList.sort(key=lambda z: (z.goalCost)) #greedy search
        if searchAlgorithm == 4:
            openList.sort(key=lambda z: (z.totalCost)) #A* search

cellList[endRow][endCol].cellType = 'G'  #Ending point
cellTraverse = cellList[endRow][endCol].priorCell

totalCost = cellList[endRow][endCol].cost  #Total cost to get to endRow and endCol
totalSteps = 0

#Path chosen gets updated information such as total coast
#total steps, and a happy face
while cellTraverse:
    cellTraverse.cellType = '☺'
    totalCost += cellTraverse.cost
    totalSteps += 1
    cellTraverse = cellTraverse.priorCell

cellList[startRow][startCol].cellType = 'S'   #Starting point

#lines below are essentially easy to read 2d for loop
for y in range(column):
    for x in range(row):
        cellList[x][y].printSelf() #print out each cell
    print()
print_results()
f.close()

