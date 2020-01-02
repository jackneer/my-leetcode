def is_match(s, p):

    si = 0
    pi = 0
    match = True
    keys = []

    while pi < len(p):
        if p[pi] == '.':
            keys.append(p[pi])
        elif p[pi] == '*':
            keys[len(keys) - 1] += '*'
        else:
            keys.append(p[pi])
        pi += 1
    
    for key in keys:
        if key == '.':
            si += 1
        elif '*' in key:
            for i in range(si, len(s)):
                if compare(s[si], key[0]):
                    si += 1
                else:
                    break
        else:
            if compare(s[si], key):
                si += 1
            else:
                match = False
                break

    if si < len(s):
        match = False

    return match


def compare(s1, s2):
    if s1 == s2:
        return True
    elif s1 == '.' or s2 == '.':
        return True
    else:
        return False       


def main():    
    print(is_match("aa", "a"))
    print(is_match("aa", "a*"))
    print(is_match("ab", ".*"))
    print(is_match("aab", "c*a*b"))
    print(is_match("mississippi", "mis*is*p*."))


if __name__ == '__main__':
    main()