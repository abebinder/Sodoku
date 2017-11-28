import sys
from array import array
sodoku_array=[] 
possibles_array=[]

def initialize_sodoku_array():
    with open(theFileName, "r") as ins:
        
        for i in range(0, 9):
            sodoku_array.append([])
        i=0
        miniarray=[]
        for line in ins:
            miniarray=line.split()
            newarray=[]
            for ii in miniarray:
                newarray.append( int(ii))
            sodoku_array[i]=newarray
            i=i+1

def initialize_possibles_array():
    for i in range(0, 9):
        possibles_array.append([])
    for i in  range(0, 9):
        for  j in range(0,9):
            possibles_array[i].append([])
                       
def solve(arr):
    
    for i  in range(0,10):
        arr= firstLevelSolve(arr)
    
    arr=recursiveSolve(arr)
    return arr

def printArray(arr):
    i=0
    for i in range(0,9):
        for j in range(0, 9):
            sys.stdout.write(str(arr[i][j])+" ")
        print("")

def checkRow(guess, arr, row):
    for i in range(0, 9):
        if(arr[row][i]==guess):
            return False
    return True

def checkColumn(guess, arr, column):
    for i in range(0, 9):
        if(arr[i][column]==guess):
            return False
    return True

def checkBlock(guess, arr, row, column):
    if(row<3 and column<3):
        for i in range(0,3):
            for j in range(0,3):
                if (arr[i][j]==guess):
                    return False
    elif((3<=row<6)and column<3):
        for i in range(3,6):
            for j in range(0, 3):
                if(arr[i][j]==guess):
                    return False
    elif((6<=row<9)and column<3):
        if(blockCheckHelper(arr, guess, 6, 9, 0, 3)==False):
            return False
    elif((row<3)and 3<=column<6):
        if(blockCheckHelper(arr, guess, 0, 3, 3, 6)==False):
            return False
    elif((3<=row<6)and 3<=column<6):
        if(blockCheckHelper(arr, guess, 3, 6, 3, 6)==False):
            return False
    elif((6<=row<=9)and 3<=column<6):
        if(blockCheckHelper(arr, guess, 6, 9, 3, 6)==False):
            return False
    elif((row<3)and 6<=column<9):
        if(blockCheckHelper(arr, guess, 0, 3, 6, 9)==False):
            return False
    elif((3<=row<6)and 6<=column<9):
        if(blockCheckHelper(arr, guess, 3, 6, 6, 9)==False):
            return False
    elif((6<=row<9)and 6<=column<9):
        if(blockCheckHelper(arr, guess, 6, 9, 6, 9)==False):
            return False
    return True

def blockCheckHelper(arr, guess, istart, iend, jstart, jend):
    for i in range(istart,iend):
            for j in range(jstart, jend):
                if(arr[i][j]==guess):
                    return False

def check(arr, guess, row, column):
    if(checkBlock(guess, arr, row, column)==True and checkColumn(guess, arr, column)==True and checkRow(guess, arr, row)==True):
        return True
    else:
        return False

def printLoopCheck():
    for i in range(0, 9):
        for j in range(0,9):
            if(sodoku_array[i][j]==0):
                print(check(sodoku_array, 8, i, j))
        
        print("row finished")

def checkAllPossibleValuesForOneSpot(arr, row, column):
    possibleList=[]
    if(arr[row][column]==0):
        for i in range(1, 10):
            if(check(arr, i, row, column)):
                possibleList.append(i)
    return possibleList

def firstLevelSolve(arr):
    keepgoing=True
    while keepgoing:
        keepgoing=False
        for i in range(0, 9):
            for j in range(0, 9):
                if(arr[i][j]==0):
                    possibles_array[i][j]=(checkAllPossibleValuesForOneSpot(arr, i, j))
                    if(len(possibles_array[i][j])==1):
                        keepgoing=True
                        arr[i][j]=possibles_array[i][j][0]
                if(i==8 and j==8):
                    keepgoing=False
    return arr

def isSolved(arr):
    for i in range(0,9):
        for  j in range(0,9):
            if(arr[i][j]==0):
                return False
    return True

def recursiveSolve(arr):
    if(isSolved(arr)):
        return arr
    else:
        for i in range(0, 9):
            for j in range(0, 9):
                if(arr[i][j]==0):
                    possibles_array[i][j]=(checkAllPossibleValuesForOneSpot(arr, i, j))
                    if(possibles_array[i][j]==[]):
                        return arr
                    else:
                        for k in range(0, len(possibles_array[i][j])):
                            arr[i][j]=possibles_array[i][j][k]
                            arr=recursiveSolve(arr)
                            if(isSolved(arr)):
                                return arr
                            
                        arr[i][j]=0
                        possibles_array[i][j]=[]
                        return arr

theFileName=input("enter filename of where sodoku puzzle is stored\n")
initialize_sodoku_array()
initialize_possibles_array()
sodoku_array= recursiveSolve(sodoku_array)
printArray(sodoku_array)
