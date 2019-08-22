input1 = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]



def find_empty(input1):
    for i in range(len(input1)):
        for j in range(len(input1[0])):
            if input1[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve(input1):
    find = find_empty(input1)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(input1, i, (row, col)):
            input1[row][col] = i

            if solve(input1):
                return True

                input1[row][col] = 0

    return False


def valid(input1, num, pos):
    # Check row
    for i in range(len(input1[0])):
        if input1[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for j in range(len(input1)):
        if input1[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = 3 * (i// 3)
    box_y = 3 * (j// 3)
    # secTopX, secTo0pY = 3 * (i // 3), 3 * (j // 3)

    for i in range(box_y, box_y):
        for j in range(box_x, box_x):
            if input1[i][j] == num and (i,j) != pos:
                return False

    return True




print(input1)
solve(input1)
for i in input1:
    print(i,end='\n')
