def pow(x, n):
    sign = 1

    if n < 0:
        sign = -1

    un = abs(n)

    result = 0.0

    for i in range(un + 1):
        if i == 0:
            result = 1.0
        else:
            if sign > 0:
                result *= x
            else:
                result /= x

    return result


def main():
    print(pow(2, 10))
    print(pow(2.1, 3))
    print(pow(2, -2))


if __name__ == '__main__':
    main()