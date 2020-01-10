def divide(dividend, divisor):    
    sign = 1

    if dividend * divisor < 0:
        sign = -1

    quotient = 0
    remainder = abs(dividend)
    abs_divisor = abs(divisor)

    while remainder >= abs_divisor:
        remainder -= abs_divisor
        quotient += 1

    return quotient * sign


def main():
    print(divide(dividend = 10, divisor = 3))
    print(divide(dividend = 7, divisor = -3))
    pass


if __name__ == '__main__':
    main()