def length_longest_substring(input):    
    temp = []
    longest = ''
    
    for char in input:
        if char in temp:
            if len(longest) < len(temp):
                longest = ''.join(temp)

            temp = []

        temp.append(char)
    
    print(longest)


def main():
    length_longest_substring('abcabcbb')
    length_longest_substring('bbbbb')
    length_longest_substring('pwwkew')
    pass


if __name__ == '__main__':
    main()
