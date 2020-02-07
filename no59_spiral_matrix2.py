def spiral(n):
    # array size = n x n    
    half_n = int(n / 2)

    result = [[0 for x in range(n)] for y in range(n)]

    current = 1

    for i in range(half_n):
        col = None

        for j in range(i, n - i):
            result[i][j] = current
            current += 1
            col = j
        
        for k in range(i + 1, n - i - 1):            
            result[k][j] = current
            current += 1

        for l in range(n - i - 1, i - 1, -1):
            result[n - i - 1][l] = current
            current += 1
            col = l

        for o in range(n - i - 2, i, -1):
            result[o][l] = current
            current += 1
    
    if n != (half_n * 2):
        for p in range(half_n, n - half_n):
            result[half_n][p] = current
            current += 1
    
    return result


def main():
    print(spiral(3))
    print(spiral(4))


if __name__ == '__main__':
    main()