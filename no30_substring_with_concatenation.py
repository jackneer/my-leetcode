def substring(s, words):
    start_indices = []

    for item in  build(len(words), words):
        temp = ''.join(item)
        index = s.find(temp)

        if index >= 0:
            start_indices.append(index)

    return start_indices


def build(num, words):
    if num == 1:
        return [words]
    else:
        all = []

        for i in range(num):
            temp = []

            for j in range(i + 1, num + i):
                temp.append(words[j % num])

            buf = build(num - 1, temp)

            for item in buf:
                item.append(words[i])
                all.append(item)

        return all


def main():
    print(substring(s = "barfoothefoobarman", words = ["foo","bar"]))
    print(substring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))


if __name__ == '__main__':
    main()