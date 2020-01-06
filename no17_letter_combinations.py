def letter_combinations(num):
    phone_nums = { '1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': []}

    temp_nums = []
    result = []

    for letter in num:
        temp = phone_nums.get(letter)

        if temp is not None and len(temp) > 0:
            temp_nums.append(temp)

    print(temp_nums)

    result = temp_nums[0]

    for ti in range(1, len(temp_nums)):
        result = product(result, temp_nums[ti])

    return result


def product(array1, array2):
    result = []
    for i in range(len(array1)):        
        for j in range(len(array2)):
            result.append(array1[i] + array2[j])

    return result


def main():    
    print(letter_combinations('23'))
    print(letter_combinations('79'))


if __name__ == '__main__':
    main()