def atoi(input):
    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', ' ']
    temp = []

    for char in input:
        if char in valid_chars:
            if char != ' ':
                temp.append(char)            
        else:
            break

    sign = 1

    result = 0

    if len(temp) > 0:
        if temp[0] == '-':
            sign = -1

        if temp[0] == '-' or temp[0] == '+':
            temp.pop(0)

        max_signed_int = 2**31
        max_signed_int_str = str(max_signed_int)        

        if len(temp) > len(max_signed_int_str):
            result = max_signed_int * sign
        elif len(temp) < len(max_signed_int_str):
            result = int(''.join(temp)) * sign
        else:
            for i in range(0, len(temp)):
                if temp[i] > max_signed_int_str[i]:
                    result = max_signed_int * sign
                    break
            
            if result == 0:
                result = int(''.join(temp)) * sign

    return result


def main():
    print(atoi('42'))
    print(atoi('   -42'))
    print(atoi('4193 with words'))
    print(atoi('words and 987'))
    print(atoi('-91283472332'))
    print(atoi('-2147483647'))
    pass


if __name__ == '__main__':
    main()