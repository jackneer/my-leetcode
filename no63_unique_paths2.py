def unique_paths_init(map):
    return unique_paths(map, len(map[0]), len(map))


def unique_paths(map, m, n):
    if m == 1 and n == 1:
        return 1
    elif m > 0 and n > 0:
        if map[m - 1][n - 1] == 1:
            return 0
        else:
            return unique_paths(map, m - 1, n) + unique_paths(map, m, n - 1)
    else:
        return 0      

def main():
    print(unique_paths_init([[0,0,0],[0,1,0],[0,0,0]]))


if __name__ == '__main__':
    main()