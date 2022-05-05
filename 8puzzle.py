import queue
import time

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

def misTiles(state):
    return 0

def eucledDist(state):
    return 0

def aStar(puz: Puzzle, addNodes):
    return 0

def addNodes(queue, families, depth):
    for family in families:
        queue.put(searchFunction(family[0]) + depth, depth, family)
    return queue

#global variables
searchFunction = uniformCost
maxQSize = 0
nodesExpand = 0

def main():
    global searchFunction
    print('Welcome to Angela Su 8 puzzle solver.')

#get the user inputs for default or user puzzle
    userInput = input('Type "1" to use default puzzle, or "2" to enter your own puzzle.')
    userNum = int(userInput) 

    #Basic Puzzle (if userInput is 1)
    if userNum == 1:
        puz = (['1', '2', '3'], ['4', '0', '6'], ['7', '5', '8'])
    #Custom Puzzle (if userInput is 2)
    elif userNum == 2:
        print('Enter your puzzle, use a zero to represent the blank\n')
        row1 = input('Enter the first row, use space or tabs between numbers')
        row2 = input('Enter the second row, use space or tabs between numbers')
        row3 = input('Enter the third row, use space or tabs between numbers')

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
    alg = int(userAlg)

    #run the algorithm of choice and print the output
    if(alg == '1'):
        print('Run Uniform Cost Search \n')
        searchFunction = uniformCost

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

    elif(alg == '2'):
        print('Run A* with the Misplaced Tile heuristic \n')
        searchFunction = misTiles

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

    elif(alg == '3'):
        print('Run A* with the Eucledian distance heuristic  \n')
        searchFunction = eucledDist

        start = time.time()
        node = aStar(userPuzzle, addNodes)
        end = time.time()

        printResults(node, start, end)

if __name__ == "__main__":
    main()