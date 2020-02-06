def nqueens(n):
    result = []
    
    for ri_start in range(n):
        for ci_start in range(n):

            board = [['.' for x in range(n)] for y in range(n)]
            count = 0
            half_row_max_col = 0

            for ri in range(n):
                if ri < ri_start:
                    continue

                for ci in range(n):
                    if ri == ri_start and ci < ci_start:
                        continue

                    if ri < (n / 2) and ci <= half_row_max_col:
                        continue

                    if check(board, ri, ci, n):
                        board[ri][ci] = 'Q'
                        count += 1

                        if ri < (n / 2):
                            half_row_max_col = ci
           
            if count == n:
                result.append(board)

    return len(result)


def check(board, row, col, n):
    for i in range(n):
        if board[i][col] == 'Q':
            return False
        if board[row][i] == 'Q':
            return False
        
        if i > 0:
            if i + row < n:
                if i + col < n:
                    if board[i + row][i + col] == 'Q':
                        return False
                if col - i >= 0:
                    if board[i + row][col - i] == 'Q':
                        return False
            if row - i >= 0:
                if i + col < n:
                    if board[row - i][i + col] == 'Q':
                        return False
                if col - i >= 0:
                    if board[row - i][col - i] == 'Q':
                        return False

    return True


def main():
    print(nqueens(8))


if __name__ == '__main__':
    main()
