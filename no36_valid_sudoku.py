def valid_sudoku(lists):    
    # rows
    for row in lists:
        if check_block(row) == False:
            return False

    # cols
    for col_index in range(len(lists[0])):
        temp = []

        for row_index in range(len(lists)):
            temp.append(lists[row_index][col_index])
        
        if check_block(temp) == False:
            return False

    # 3x3
    for i in range(3):
        for j in range(3):
            temp = []

            for x in range(3):
                for y in range(3):
                    temp.append(lists[i * 3 + x][j * 3 + y])                    
            
            if check_block(temp) == False:
                return False

    return True


def check_block(list):
    check_dict = {}
    valid = True

    for item in list:
        if item != '.':
            if item in check_dict:
                valid = False
                break
            else:
                check_dict[item] = 0
    
    return valid


def main():    
    result = valid_sudoku([
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
    print(result)


if __name__ == '__main__':
    main()