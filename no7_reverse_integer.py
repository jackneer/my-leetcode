def reverse(num):
    n = abs(num)
    temp = []
    
    while n != 0:
        d = int(n % 10)
        temp.append(d)
        n = int(n / 10)
    
    d_multiplier = 10 ** (len(temp) - 1)
    sum = 0

    for d in temp:
        sum += int(d * d_multiplier)
        d_multiplier /= 10

    if num < 0:
        sum *= -1

    return sum


def main():    
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    pass


if __name__ == '__main__':
    main()