def justify(words, width):
    start = 0
    end = 1
    target = len(words) - 1
    result = []
    
    while start <= target or end <= target:
        temp = []
        temp = words[start: end]

        if get_length(temp) <= width:
            if end <= target:
                end += 1
            else:
                temp = words[start: end]
                result.append(justify_line(temp, width, end == len(words)))
                break
        else:
            end -= 1
            temp = words[start: end]
            result.append(justify_line(temp, width, end == len(words)))
            
            start = end
            end += 1

    return result


def get_length(words):
    sum = 0

    for word in words:
        sum += len(word)
        sum +=1
    
    sum -= 1
    return sum


def justify_line(words, width, last_line):
    temp = ' '.join(words)

    if len(words) >= 2 and not last_line:
        short = width - len(temp)

        if short > 0:
            fill = int(short / (len(words) - 1))
            leftover = short - fill * (len(words) - 1)
            if fill > 0:
                temp = temp.replace(' ', ' ' * (fill + 1))
            
            if leftover > 0:
                temp = temp.replace(' ' * (fill + 1), ' ' * (fill + 2), leftover)
    else:
        short = width - len(temp)
        temp += ' ' * short

    return [temp]


def main():
    print(justify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(justify(["What","must","be","acknowledgment","shall","be"], 16))
    print(justify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20))


if __name__ == '__main__':
    main()