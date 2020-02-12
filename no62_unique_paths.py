def unique_paths(m, n):
    if m == 1 and n == 1:
        return 1
    elif m > 0 and n > 0:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)
    else:
        return 0
        

def main():
    print(unique_paths(3, 2))
    print(unique_paths(7, 3))


if __name__ == '__main__':
    main()