def lcp(strs):
    temp = []

    for i in range(len(strs[0])):
        char = strs[0][i: i + 1]
        match = True

        for j in range(1, len(strs)):
            if char != strs[j][i: i + 1]:
                match = False
                break
        
        if match:
            temp.append(char)
        else:
            break

    return ''.join(temp)


def main():
    print(lcp(["flower","flow","flight"]))
    print(lcp(["dog","racecar","car"]))


if __name__ == '__main__':
    main()