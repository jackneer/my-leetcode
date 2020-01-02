def palindrome_number_check(num):

    if num < 0:
        return False
    
    temp = []
    number = num

    while number != 0:
        digi = number % 10
        temp.append(digi)
        number = int(number / 10)

    palindrome = True

    for i in range(0, int(len(temp) / 2)):
        if temp[i] != temp[len(temp) - 1 - i]:
            palindrome = False
            break
    
    return palindrome


# without converting number to string
def palindrome_number_check2(num):
    if num < 0:
        return False
    
    reversed = 0
    number = num
    
    while number != 0:
        digi = number % 10
        reversed = reversed * 10 + digi
        number = int(number / 10)
    
    if reversed == num:
        return True
    else:
        return False


def main():
    print(palindrome_number_check(121))
    print(palindrome_number_check(-121))
    print(palindrome_number_check(10))
    print(palindrome_number_check(5))
    print(palindrome_number_check(1235321))

    print(palindrome_number_check2(121))
    print(palindrome_number_check2(-121))
    print(palindrome_number_check2(10))
    print(palindrome_number_check2(5))
    print(palindrome_number_check2(1235321))
    pass


if __name__ == '__main__':
    main()