def length_last(words):
    items = words.split(' ')

    if len(items) > 0:
        return len(items[len(items) - 1])
    else:
        return 0


def main():
    print(length_last('Hello World'))


if __name__ == '__main__':
    main()