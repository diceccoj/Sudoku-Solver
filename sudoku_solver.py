

#SAMPLE BOARDS

board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

board2 = [
    [0, 0, 0, 2, 7, 0, 1, 8, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 5, 0, 7],
    [9, 3, 0, 0, 0, 0, 0, 2, 0],
    [4, 5, 0, 7, 0, 8, 6, 9, 1],
    [6, 8, 0, 4, 9, 2, 7, 0, 3],
    [0, 0, 8, 9, 5, 0, 0, 0, 6],
    [7, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 0, 6, 3, 0, 7, 0, 0, 0],
]

board3 = [
    [1, 6, 0, 0, 0, 2, 0, 0, 0],
    [0, 9, 2, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 8, 4, 0, 7, 0, 0, 0],
    [4, 1, 0, 2, 0, 3, 7, 5, 8],
    [9, 3, 7, 6, 0, 5, 0, 1, 2],
    [0, 0, 9, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 3, 8, 0, 4, 1],
    [3, 0, 0, 0, 2, 0, 6, 7, 0],
]



#print board
def print_board(bo):
    for i in range(len(bo)):
        if (i%3 == 0) and (i!=0):
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if (j%3 == 0) and (j != 0):
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


#returns coordinates of empty box
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

#checks if board is valid given a position
def valid(bo, num, pos):

    #check columns
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check rows
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 boxes
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range (box_y*3, box_y*3 + 3):
        for j in range (box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


#board solver
def solve(bo):

    #base case
    if (not find_empty(bo)):
        return True

    #recursive step
    else:
        row, col = find_empty(bo)
    
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False




def main():

    print("Welcome to the sudoku solver!")   

    print("Please type in the number of the sample board you would\nlike to solve, or type 'q' to quit.")
    userinput = input()

    print("\n+=+=+=+=+=+=+=+=+=+=+=+\n")
    if userinput == 'q':
        print("Quitting program...")
    elif userinput == '1':
        solve(board1)
        print_board(board1)
    elif userinput == '2':
        solve(board2)
        print_board(board2)
    elif userinput == '3':
        solve(board3)
        print_board(board3)
    else:
        print("That is not a valid input.")

    
    print("\n+=+=+=+=+=+=+=+=+=+=+=+")



    return 0

main()