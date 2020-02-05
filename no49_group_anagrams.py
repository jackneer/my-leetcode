def group(input):
    unique = []
    result = []

    for item in input:
        temp = ''.join(sorted(item))

        if temp not in unique:
            unique.append(temp)
            result.append([item])
        else:
            index = unique.index(temp)
            result[index].append(item)

    return result


def main():
    print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()