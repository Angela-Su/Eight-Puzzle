import queue
import time
from tkinter.font import families

#NOTES:
#node : h(n), g(n)
#state: list of puzzle board
#family/fam (index 0): "child" state and "parent" state (index 1)

def swap(state, index1, index2):
    temp = state.copy()
    temp[index1], temp[index2] = state[index2], state[index1]
    return temp

class Puzzle:
    goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initialState = [1, 2, 3, 4, 0, 6, 7, 5, 8]

    def print(state):
        for i in range(0, len(state), 3):
            print(state[i : i + 3])
    
    #boundary checks the blank(0) then swap if valid then swap
    #else return original list

    def leftShift(fam, zeroIndex):
        if(zeroIndex % 3 != 0):
            return swap(fam[0], zeroIndex, zeroIndex - 1)
        else: 
            return []
    
    def rightShift(fam, zeroIndex):
        if(zeroIndex % 3 != 2):
            return swap(fam[0], zeroIndex, zeroIndex + 1)
        else: 
            return []

    def upShift(fam, zeroIndex):
        if(zeroIndex > 2):
            return swap(fam[0], zeroIndex, zeroIndex - 3)
        else: 
            return []

    def downShift(fam, zeroIndex):
        if(zeroIndex < 6):
            return swap(fam[0], zeroIndex, zeroIndex + 3)
        else: 
            return []


def printResults(node, start, end):
    print("\nGoal! \n")
    print(f"To solve this problem the search algorithm expanded a total of {nodesExpand} nodes. \n")
    print(f"The maximum number of nodes in the queue at any time: {maxQSize}. \n")
    print(f"The depth of the goal node was {node[1]}.\n")

def uniformCost(state):
    return 0

#return sum of differences btw current and goal (dont include zeroStates)
def misTiles(state):
    diffs = 0
    for i in range(len(state)):
        if(state[i] != 0 and state[i] != i + 1):
            diffs += 1
    return diffs

def eucledDist(state):
    return 0

#main beef alg
def aStar(puz: Puzzle, addNodes):
    global maxQSize
    global nodesExpand

    #use the q lib
    nodes = queue.PriorityQueue()

    #check the order of the nodes
    nodes.put(createNode([puz.initialState, [0]], 0))

    while(1):
        if (nodes.empty()):
            print("no solution")
            return -1
        else:
            node = nodes.get()
            print(f"The best state to expand with a g(n) = {node[1]} and h(n) = {node[0] - node[1]} is...")
            puz.print(node[2][0])
            if (misTiles(node[2][0]) == 0): 
                return node
            else:
                nodesExpand += 1
                nodes = addNodes(nodes, expand(node[2]), node[1] + 1)
                if nodes.qsize() > maxQueueSize:
                    maxQueueSize = nodes.qsize()

def createNode(fam, depth):
    return [searchFunction(fam[0]) + depth, depth, fam]


def addNodes(queue, families, depth):
    for fam in families:
        queue.put(createNode(fam, depth))
    return queue

def expand(fam):
    families = []
    ops = [Puzzle.downShift, Puzzle.leftShift, Puzzle.rightShift, Puzzle.upShift]
    child = fam[0]
    parent = fam[1]
    zeroIndex = child.index(0)

    #cuts down on branches, dont compare gChild with gParent
    for shift in ops:
        gChild = shift(fam, zeroIndex)
        if(not isEqual(gChild, parent)):
            families.append([gChild, child])
    return families

def isEqual(state1, state2):
    for i in range(len(state1)):
        if(state1[i] != state2[i] or len(state1) != len(state2)):
            return False
    return True

#global variables
searchFunction = uniformCost
maxQSize = 0
nodesExpand = 0

def main():
    global searchFunction
    print('Welcome to Angela Su 8 puzzle solver.')

#get the user inputs for default or user puzzle
    userInput = input('Type "1" to use default puzzle, or "2" to enter your own puzzle.\n')
    userNum = int(userInput) 

    #Basic Puzzle (if userInput is 1)
    if userNum == 1:
        puz = (['1', '2', '3'], ['4', '0', '6'], ['7', '5', '8'])
    #Custom Puzzle (if userInput is 2)
    elif userNum == 2:
        print('Enter your puzzle, use a zero to represent the blank')
        row1 = input('Enter the first row, use space or tabs between numbers ')
        row2 = input('Enter the second row, use space or tabs between numbers ')
        row3 = input('Enter the third row, use space or tabs between numbers ')

        print('\n')

        #splits a string into a list based on whitespace
        row1 = row1.split()
        row2 = row2.split()
        row3 = row3.split()

        #combine rows 
        puz = row1, row2, row3
    
    userPuzzle = Puzzle 
    userPuzzle.initialState = puz
        
    #user choose algorithm
    userAlg = input('Enter your choice of algorithm \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Eucledian distance heuristic. \n')

    #chance input to a number
    #alg = int(userAlg)

    #run the algorithm of choice and print the output
    if(userAlg == '1'):
        print('Run Uniform Cost Search \n')
        searchFunction = uniformCost

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

    elif(userAlg == '2'):
        print('Run A* with the Misplaced Tile heuristic \n')
        searchFunction = misTiles

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

    elif(userAlg == '3'):
        print('Run A* with the Eucledian distance heuristic  \n')
        searchFunction = eucledDist

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

if __name__ == "__main__":
    main()