def match(s, p):
    s_index = 0
    matched = True

    for p_index in range(len(p)):
        if p[p_index] == '?':
            if s[s_index] is not None:
                s_index += 1
            else:
                matched = False
                break
        elif p[p_index] == '*':
            if (p_index + 1) < len(p):
                while s_index < len(s):
                    if s[s_index] == p[p_index + 1]:
                        p_index += 1
                        break
                    else:
                        s_index += 1

                if s_index >= len(s):
                    matched = False
                    break
            else:
                s_index = len(s)
        else:
            if s[s_index] == p[p_index]:
                s_index += 1
            else:
                matched = False
                break

    if s_index < len(s):
        matched = False

    return matched


def main():    
    print(match("aa", "a"))
    print(match("aa", "*"))
    print(match("cb", "?a"))
    print(match("adceb", "a*b"))
    print(match("acdcb", "a*c?b"))


if __name__ == '__main__':
    main()