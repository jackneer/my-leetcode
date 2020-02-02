def multiply_string(num1, num2):    
    product = 0    
    num1_digit = 1

    for num1_char in reversed(num1):
        num1_char_val = ord(num1_char) - 48
        num2_digit = num1_digit

        for num2_char in reversed(num2):
            num2_char_val = ord(num2_char) - 48
            product += num1_char_val * num2_char_val * num2_digit

            num2_digit *= 10
        
        num1_digit *= 10

    return product


def main():
    print(multiply_string('2', '3'))
    print(multiply_string('123', '456'))


if __name__ == '__main__':
    main()