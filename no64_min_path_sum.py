def unique_paths_init(map):
    return min(unique_paths(map, len(map[0]), len(map)))


def unique_paths(map, m, n):
    if m == 1 and n == 1:
        return [map[m - 1][n - 1]]
    elif m > 0 and n > 0:
        t1 = unique_paths(map, m - 1, n)
        t2 = unique_paths(map, m, n - 1)
        
        return [t + map[m - 1][n - 1] for t in t1] + [t + map[m - 1][n - 1] for t in t2]
    else:
        return []


def main():
    print(unique_paths_init([[1,3,1],[1,5,1],[4,2,1]]))


if __name__ == '__main__':
    main()