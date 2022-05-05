
def main():
    print('Welxome to Angela Su 862119568 8 puzzle solver.')

#get the user inputs for default or user puzzle
    userInput = input('Type "1" to use default puzzle, or "2" to enter your own puzzle.')
    userNum = int(userInput) 

    #Basic Puzzle (if userInput is 1)
    if userNum == 1:
        puzzle = (['1', '2', '3'], ['4', '0', '6'], ['7', '5', '8'])
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
        puzzle = row1, row2, row3

    #user choose algorithm
    userAlg = input('Enter your choice of algorithm \n'
                    '1) Uniform Cost Search \n'
                    '2) A* with the Misplaced Tile heuristic. \n'
                    '3) A* with the Eucledian distance heuristic. \n')

    #chance input to a number
    alg = int(userAlg)

    #run the algorithm of choice and print the output
    