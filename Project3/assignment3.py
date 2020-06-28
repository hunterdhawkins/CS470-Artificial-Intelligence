import copy
import xlrd
import pandas
import csv
import numpy
import math
import random
import time

numColors = 7   #Maximum number of colors
usedNumOfColor =0   #used with DFS
colorIncrement =1   #used with Hill Climbing
assignments = 0
runTime =0
numOfRows =0    #number of rows in map
numOfColumns =0 #number of columns in map
solution = []   #used for initial solutions
RowSum = []     #used to count neighbors
map1 = []   #read in map into this

#count the number of conflicting regions
#Helper function
def count_conflicts(m,sol):
    conflicts = 0
    for i in range(0,numOfColumns): #looking at each region, counting down the rows
        for j in range(i+1, numOfRows): #working accross columns
            if(m[i][j] == 1): #The regions are connected
                if(sol[i] == sol[j] and sol[i] != -1 and sol[j] != -1): #given same color
                    conflicts +=1
    return conflicts


#checks to see if all of the regions are assigned a color
#if they are return true, otherwise return false
def fully_assigned(s):
    for i in range(0,len(s)):
        if s[i] == -1:
            return False
    return True


#s is initial solution, starts at all values being -1
#var is the region that we want to assign a color too
#DepthFirstSearch with Degree Heuristic: Maixmum Constrained Variable
#Step 1: Look for region with most connections, and assign it a color
#Step 2: Keep performing step 1 until there is an issue than assign it a new color
#Step 3: Once all regions are assigned a color return True, otherwise return False
def MaxConstrainedDFS(s):
    global usedNumOfColor
    global assignments
    #print("Remaining regions", RowSum)
    var = RowSum.index(max(RowSum))  # This is the index of the row that has the highest number of neighbors
    #countZero = not numpy.any(RowSum)   #Calculate out which values are zero in Row sum
    count = all(number == -1 for number in RowSum)
    usedNumOfColor = (max(s) + 1)
    while count != True :#If the value list is not empty
        for c in range(0,numColors):    #for loop to try all the colors
            s2 = copy.deepcopy(s)   #copy the solution
            s2[var] = c #try to get temp solution at location of variable a color value
            print("The region being assigned a color is", var,s2, "The number of conflicts are",count_conflicts(map1, s2))
            if(count_conflicts(map1, s2) == 0): #no conflicts, yet
                #found solution or havent assigned all variables yet in which case need to continue recursing through tree
                if(fully_assigned(s2) == True):
                    print("The solution is ", s2)
                    return True
                    break
                else:
                    assignments += 1
                    RowSum[var] = -1
                    #print("Popped Region",var, "off of the value list as it has the most neighbors")
                    #print("The new value list is", RowSum)
                    temp =  MaxConstrainedDFS(s2)    #if leaf node returns true, we found a solution
                    #if false will get to end of for loop and try assigning another color
                    if (temp == True):
                        #print("The amount of time it took was ", time.time() - runTime, "Seconds")
                        return True
                        break
        return False #Cannot assign it a color, no solution found



#count the neighbors each region has by summing the rows
def neighbor_count(m):
    rows = len(m)
    cols = len(m[0])
    for i in range(0,rows):
        sumRow = 0
        for j in range(0,cols):
            sumRow = sumRow + m[i][j]
        #print( "Region", str(i), "has", str (sumRow), "neighbors")
        """if sumRow ==0:  #if there is no neighbors
            sumRow[i] = random.randint(1,numColors) #give it a value of 9"""

        RowSum.append(sumRow)

# Simple Hill climbing algorithm
#Step 1: Create an initial state and value it. If goal state break
#Step 2: Loop through steps 3 and 4 until a solution is found or there is no more colors
#Step 3: Generate new random state
#Step 4: With the state in step 3, if its a goal state return, if it has less conflicts make it current state, if not better keep looping
def hillClimbing(s, timeToSearch):
    global numColors
    global colorIncrement
    global assignments
    global runTime
    t_end = time.time() + (timeToSearch)   #will run for user seconds for each color until found solution
    runTime = time.time()

    initSol = copy.deepcopy(s)  # create an initial solution
    tempSol = copy.deepcopy(s)  #create a temp solution
    generateRandArr(initSol,colorIncrement) # generate a random initial solution with values between 0 and 1
    initConflict = count_conflicts(map1, initSol)
    tempConflict =0
    while (colorIncrement <= numColors):
        if count_conflicts(map1,initSol) ==0:   #if there is no conflicts with the solution
            #print("We found no conflicts with this solution:")
            print("The first randomly generated solution found is", initSol)
            print("The amount of time taken was ", time.time() - runTime, "Seconds")
            return True
            break
        if(colorIncrement == numColors):
            print("The amount of time taken was ", time.time() - runTime, "Seconds")
            return False
            break
        else:   #conflicts found
            while (time.time() < t_end): #while loop used to run for certain number of seconds than start adding in new colors
                #print("Generating array with ", colorIncrement +1, "colors")
                generateRandArr(tempSol,colorIncrement)
                assignments +=1
                tempConflict = count_conflicts(map1, tempSol)
                print( "The randomly generated solution is ", tempSol)
                print("The number of conflicts in it is ", tempConflict)
                #if there is less conflicts in the temp
                if tempConflict < initConflict:
                    initConflict = tempConflict #set new number of conflicts as min
                    #print("Reassigning solution")
                    initSol = copy.deepcopy(tempSol)    #copy temp solution to init solution

        colorIncrement +=1
        t_end += timeToSearch



#This function is used in the hill climbing algorithm to generate random solutions
def generateRandArr(arr, allowedColors):
    for i in range(len(arr)):
        arr[i] = random.randint(0,allowedColors)

    return arr


#This function is used to read in the file given and store it in a global array
def read_in_file1():
    global map1
    global solution
    global numOfRows
    global numOfColumns
    df = pandas.read_csv("CSPData.csv") #Read in file and store in variable
    numOfRows = len(df)
    numOfColumns = len(df.columns)    #Figure out the number of rows and columns
    solution = numpy.full(numOfRows, -1)
    #print (solution)
    A = numpy.array(df)  #Turn read in file to array
    A.reshape(numOfColumns, numOfRows)  #reshape the array to a 2d array with the num of rows and cols
    map1 = copy.deepcopy(A)



#Start of "int main" so to speak
print("Starting up the program")
read_in_file1()
print("Which type of CSP would you like to use")
print (" 1 = Depth First Search W/ Degree Heuristic, 2 = Hill Climbing")
userInput = int(input())
if userInput == 1:
    runTime = time.time()
    neighbor_count(map1)
    solution = MaxConstrainedDFS(solution)
    if solution == False:
        print("No solution found with ", numColors, "colors")
        print("The number of conflicts addressed was:", assignments)
        print("The amount of time taken was ", time.time() - runTime, "Seconds")
    else:
        print("Solution possible with ", usedNumOfColor, "colors")
        print("The number of conflicts addressed was: ", assignments)
        print("The amount of time taken was ", time.time() - runTime, "Seconds")
if userInput == 2:
    print("How long do you want to search for (in seconds) before adding in additional colors?")
    print("In most cases 5-6 seconds per color finds a solution")
    userTimeInput = int(input())
    solution2 = hillClimbing(solution,userTimeInput)
    if solution2 == False:
        print("No solution found with ", numColors)
        print("The number of randomly assigned solutions created and checked was: ", assignments)
    else:
        print("Solution possible with ",colorIncrement , "colors")
        print("The number of randomly assigned solutions created and checked was: ", assignments)