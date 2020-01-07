def check(input):
    
    brackets = { ')': '(', '}': '{', ']': '['}

    temp = []
    result = True

    for char in input:
        if char in brackets.values():
            temp.append(char)
        elif char in brackets:
            if temp[len(temp) - 1] == brackets.get(char):
                temp.pop(len(temp) - 1)
            else:
                result = False
                break

    return result


def main():
    print(check('()'))
    print(check('()[]{}'))
    print(check('(]'))
    print(check('([)]'))
    print(check('{[]}'))


if __name__ == '__main__':
    main()