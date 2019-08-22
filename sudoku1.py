input=[[5,1,7,6,0,0,0,3,4],
        [2,8,9,0,0,4,0,0,0],
        [3,4,6,2,0,5,0,9,0],
        [6,0,2,0,0,0,0,1,0],
        [0,3,8,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]

def findNextCellToFill(input,i,j):
    for i in range(0, 9):
        for j in range(0, 9):
            if input[i][j] == 0:
                return i,j
    return -1,-1
# def findNextCellToFill(input,i,j):
#     ((i,j) for j in range(0,9) for i in range(0,9) if input[i][j]==0)


# for i in range(len(input)):
#     for j in range(len(input[0])):
#         if input[i][j]==0:
#             print('found zeros at',i,j)
# print(findNextCellToFill(input,0,9))

def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    # print("v=solveSudoku",i,j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            # print("v of e",e)
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False
def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        # print('thsi is row',rowOk)
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                # print("this is col",columnOk)
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here.#x=3*(0//3),3*(4//3)   qw
                        # print("secX and SecY",secTopX,secTopY)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False
for i in input:
    print(i,end='\n')
print("=======================")
solveSudoku(input)
for i in input:
    print(i,end='\n')
# e=1,2,3,4,5,6,7,8,9
# for e in input:
#     for e in input:
#      print(input.count(e),end='\n')


