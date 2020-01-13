def longestValidParentheses(input):

    temp = []
    valid = []

    for i in range(len(input)):
        if input[i] == '(':
            temp.append(i)
        elif input[i] == ')':
            if len(temp) > 0:
                valid.append(temp.pop(len(temp) - 1))
                valid.append(i)

    count = 0
    max = 0

    for i in range(len(input)):        
        if i in valid:
            count += 1
            if count > max:
                max = count
        else:
            count = 0

    return max


def main():    
    print(longestValidParentheses('(()'))
    print(longestValidParentheses(')()())'))


if __name__ == '__main__':
    main()