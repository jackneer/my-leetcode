def solve_sudoku(lists):
    while True:
        done = True
        for row_index in range(len(lists)):
            for col_index in range(len(lists[0])):
                if lists[row_index][col_index] == '.':
                    possible = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    possible = check_row(lists, row_index, possible)
                    possible = check_col(lists, col_index, possible)

                    x = int(row_index / 3)
                    y = int(col_index / 3)

                    possible = check_block(lists, x, y, possible)

                    if len(possible) == 1:
                        lists[row_index][col_index] = possible[0]
                    else:
                        done = False
        if done:
            break

    return lists


def check_row(lists, row_index, possible):
    return check(lists[row_index], possible)


def check_col(lists, col_index, possible):
    temp = []

    for row_index in range(len(lists)):
            temp.append(lists[row_index][col_index])

    return check(temp, possible)


def check_block(lists, i, j, possible):
    temp = []

    for x in range(3):
        for y in range(3):
            temp.append(lists[i * 3 + x][j * 3 + y])                    
    
    return check(temp, possible)


def check(list, possible):
    
    valid = True

    for item in list:
        if item != '.':
            if item in possible:
                possible.remove(item)
                
    return possible


def main():    
    result = solve_sudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ])

    for row in result:
        print(row)


if __name__ == '__main__':
    main()