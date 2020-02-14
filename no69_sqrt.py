def sqrt(m):
    n = 1

    while (n * n) < m and ((n+1) * (n+1)) <= m :
        n += 1

    return n 
        

def main():
    print(sqrt(4))
    print(sqrt(8))


if __name__ == '__main__':
    main()