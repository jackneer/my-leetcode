def int_to_roman(num):
    roman_nums = [[1000, 'M'], [500, 'D'], [100, 'C'], [50, 'L'], [10, 'X'], [5, 'V'], [1, 'I']]
    roman = []

    for i, rn in enumerate(roman_nums):
        if i % 2 == 1:
            continue

        if num == 0:
            break

        temp_num = int(num / rn[0])

        num = num - (temp_num * rn[0])

        rn_m5 = roman_nums[i - 1]
        rn_m10 = roman_nums[i - 2]

        if temp_num >= 1 and temp_num <= 3:
            for j in range(temp_num):
                roman.append(rn[1])
        elif temp_num == 4 :            
            roman.append(rn[1] + rn_m5[1])
        elif temp_num == 5 :
            roman.append(rn_m5[1])
        elif temp_num >= 6 and temp_num <= 8:
            roman.append(rn_m5[1])
            for j in range(temp_num - 5):
                roman.append(rn[1])
        elif temp_num == 9 :
            roman.append(rn[1] + rn_m10[1])

    return ''.join(roman)


def main():    
    print(int_to_roman(3))
    print(int_to_roman(4))
    print(int_to_roman(9))
    print(int_to_roman(58))
    print(int_to_roman(1994))
    

if __name__ == '__main__':
    main()