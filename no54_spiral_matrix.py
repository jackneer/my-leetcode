def spiral(nums):
    # array size = m x n
    m = len(nums)
    n = len(nums[0])
    half_m = int(m / 2)

    result = []

    for i in range(half_m):
        col = None

        for j in range(i, n - i):
            result.append(nums[i][j])
            col = j
        
        for k in range(i + 1, m - i - 1):
            result.append(nums[k][j])

        for l in range(n - i - 1, i - 1, -1):
            result.append(nums[m - i - 1][l])
            col = l

        for o in range(m - i - 2, i, -1):
            result.append(nums[o][l])
    
    if m != (half_m * 2):
        for p in range(half_m, n - half_m):
            result.append(nums[half_m][p])
    
    return result


def main():
    print(spiral([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]))
    print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


if __name__ == '__main__':
    main()