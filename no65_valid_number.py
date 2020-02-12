number_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sign_chars = ['+', '-']
float_char = ['.']
exp_char = ['e']
qulify_chars = number_chars + sign_chars + float_char + exp_char

def valid(input):

    temp = input.lower().strip()
    syntax = []
    
    for i in range(len(temp)):
        
        if temp[i] not in qulify_chars:
            return False
        elif temp[i] in sign_chars:
            syntax.append('S')
        elif temp[i] in number_chars:
            syntax.append('N')
        elif temp[i] in float_char:
            syntax.append('F')
        elif temp[i] in exp_char:
            syntax.append('E')
    

    for i in range(len(syntax) - 1, 0, -1):
        if syntax[i] == 'N' and syntax[i - 1] == 'N':
            syntax.pop(i)

    syntax = ''.join(syntax)

    if 'ENFN' in syntax:
        return False
        
    syntax = syntax.replace('SN', 'N')
    syntax = syntax.replace('NFN', 'N')
    syntax = syntax.replace('NEN', 'N')

    if syntax == 'N':
        return True
    else:
        return False


def main():
    print(valid("0"))
    print(valid("0.1"))
    print(valid("abc"))
    print(valid("1 a"))
    print(valid("2e10"))
    print(valid(" -90e3"))
    print(valid(" 1e"))
    print(valid("e3"))
    print(valid("6e-1"))
    print(valid(" 99e2.5"))
    print(valid("53.5e93"))
    print(valid(" --6"))
    print(valid("-+3"))
    print(valid("95a54e53"))


if __name__ == '__main__':
    main()