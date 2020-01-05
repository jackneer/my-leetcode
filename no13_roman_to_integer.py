def roman_to_int(roman):
    roman_nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    num = 0
    temp_num = 0

    for i in range(len(roman)):        
        cur_num = roman_nums.get(roman[i:i+1])
        prev_num = 0

        if i > 0:
            prev_num = roman_nums.get(roman[i-1:i])

        if prev_num == 0 or prev_num == cur_num:
            temp_num += cur_num
        elif prev_num > cur_num:
            num += temp_num
            temp_num = cur_num
        elif prev_num < cur_num:
            num += cur_num - temp_num
            temp_num = 0

    if temp_num !=0:
        num += temp_num

    return num
    

def main():
    print(roman_to_int('III'))
    print(roman_to_int('IV'))
    print(roman_to_int('IX'))
    print(roman_to_int('LVIII'))
    print(roman_to_int('MCMXCIV'))


if __name__ == '__main__':
    main()