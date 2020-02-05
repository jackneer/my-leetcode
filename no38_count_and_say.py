def count_and_say(num):
    if num == 1:
        return '1'
    else:
        temp = count_and_say(num - 1)
        return process(temp)


def process(input):
    index = 0
    temp = ''

    while index < len(input):
        if index <= (len(input) - 2):
            if input[index] == input[index + 1]:
                if input[index] == '1':
                    temp += '21'
                else:
                    temp += '22'
                index += 1
            else:
                if input[index] == '1':
                    temp += '11'
                else:
                    temp += '12'
        else:
            if input[index] == '1':
                temp += '11'
            else:
                temp += '12'
        
        index += 1
    
    return temp


def main():
    for i in range(1, 6):
        print(count_and_say(i))


if __name__ == '__main__':
    main()