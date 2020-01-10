def str_str(haystack, needle):    
    if needle is None or len(needle) == 0:
        return 0

    found_index = -1

    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            found_index = i

    return found_index


def main():
    print(str_str(haystack = 'hello', needle = 'll'))
    print(str_str(haystack = 'aaaaa', needle = 'bba'))
    pass


if __name__ == '__main__':
    main()