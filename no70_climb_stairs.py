def climb(stairs):
    if stairs == 0:
        return []
    elif stairs == 1:
        return [[1]]
    elif stairs == 2:
        return [[1, 1], [2]]
    elif stairs > 2:

        temp1 = climb(stairs - 1)
        temp2 = climb(stairs - 2)

        for item1 in temp1:
            item1.append(1)

        for item2 in temp2:
            item2.append(2)

        return temp1 + temp2
        

def main():
    print(climb(2))
    print(climb(3))
    print(climb(4))


if __name__ == '__main__':
    main()