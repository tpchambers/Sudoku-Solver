#Theo#

def valid(m, numb, grid):
    
    # We pass a tuple as grid later
    #grid[0] = row
    #grid[1] = column
    
    # check row
    for i in range(len(m)):
        # check if num in row and make sure not exact position already inserted
        if m[grid[0]][i] == numb:
            #while different position
            while grid[0] != i:    
                return False
    
    # check column
    for j in range(len(m)):
        if m[i][grid[1]] == numb:
            while grid[1] != grid:
                return False
        
    # check for 3 by 3 grid positions (make sure number is not anywhere in grid)
    board_pos_x = grid[0] - grid[0] % 3
    board_pos_y = grid[1] - grid[1] % 3 
    
    for i in range(3):
        for j in range(3):
                        # check if number in grid
                       if m[board_pos_x + i][board_pos_y + j] == numb:
                           #make sure we skip over grid we just entered
                           while (board_pos_x + i, board_pos_y + j) != grid:
                               return False
    return True
    
def check_null(m):
    for i in range(len(m)):
        for j in range(len(m)):
            # if element in matrix is 0, return tuple of positions
            if m[i][j] == 0:
                return i,j 
    return False

def solve(m):
    # if there are no empty values, we are done --> return True
    if not check_null(m):
        return True
    else:
        # set tuple equal to positions returned in check_null
        r,c = check_null(m)
    for n in range(1,10):
        if valid(m,n,(r,c)):
            m[r][c]=n
            #call solve again with new value added
            if solve(m):
                # return True and pull out of loop once board filled
                return True
            # reset value if we don't return True
            m[r][c] = 0
    
        
def p_board(m):
    for line in m:
        print(line)


board = [
    [3,9,0,0,0,0,2,0,0],
    [0,7,8,3,0,0,0,0,9],
    [6,0,4,0,9,0,3,7,0],
    [0,6,0,5,0,8,9,0,0],
    [0,0,2,9,0,4,0,6,0],
    [0,8,9,0,0,0,4,3,0],
    [0,0,6,0,2,0,5,0,4],
    [5,0,0,0,0,9,7,2,0],
    [0,0,7,0,0,0,0,8,6]
]


print("=====Unsolved======")
p_board(board)
print()
print("=====Solved========")
solve(board)
p_board(board)

        
     