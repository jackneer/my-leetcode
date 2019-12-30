def longestPalindrome(input):
    longest = ''

    for i in range(0, len(input) - 1):
        for j in range(i + 1, len(input)):
            if check(input[i:j+1]) and len(longest) < (j - i + 1):
                longest = input[i:j+1]

    return longest


def check(input):
    match = True
    for i in range(0, int(len(input) / 2)):
        if input[i] != input[len(input) - 1 - i]:
            match = False
            break
    
    return match


def main():
    print(longestPalindrome('babad'))
    print(longestPalindrome('cbbd'))
    pass


if __name__ == '__main__':
    main()