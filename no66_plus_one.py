def plus_one(m):
    carry = True
    
    for i in range(len(m) - 1, -1, -1):
        if carry:
            m[i] += 1
            carry = m[i] >= 10
            m[i] = m[i] % 10

    return m
        

def main():
    print(plus_one([1,2,3]))
    print(plus_one([4,3,2,1]))


if __name__ == '__main__':
    main()