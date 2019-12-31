def convert(input_str, num_rows):
    revolution = num_rows * (num_rows - 1)
    temp = []
    index = 0
    str_index = 0

    while  str_index < len(input_str):
        if index < num_rows:
            temp.append(input_str[str_index:str_index+1])
            str_index += 1
        elif (index - (num_rows - 1)) % (num_rows - 1) == 0:
            temp.append(input_str[str_index:str_index+1])
            str_index += 1
        else:
            temp.append(' ')
        
        index += 1

        if index == revolution:
            index = 0
    
    result = []
    col_index = 0

    while len(temp) > 0:
        for row_index in range(0, num_rows):
            if col_index == 0:
                result.append([])

            if len(temp) > 0:
                result[row_index].append(temp.pop(0))
            else:
                break

        col_index += 1

    for row in result:        
        print(''.join(row))


def main():
    convert('PAHNAPLSIIGYIR', 3)
    convert('PAHNAPLSIIGYIR', 4)
    pass


if __name__ == '__main__':
    main()