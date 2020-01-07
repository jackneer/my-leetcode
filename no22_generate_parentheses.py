def gen_parentheses(num):
    breakets = ['(', ')']
    
    temp = ['(', ')']

    for i in range(1, num * 2):        
        temp = product(temp, breakets)
        purge(temp, num)

    return temp


def product(array1, array2):
    result = []

    for i in range(len(array1)):        
        for j in range(len(array2)):
            result.append(array1[i] + array2[j])

    return result


def purge(temp, num):
    for item in reversed(temp):
        remove = False
        open = 0

        for char in item:            
            if char == '(':
                open += 1
            else:
                open -= 1

            if open < 0:
                remove = True
                break            

        if item.count('(') > num or item.count(')') > num:
            remove = True

        if remove:
            temp.remove(item)


def main():    
    print(gen_parentheses(3))


if __name__ == '__main__':
    main()