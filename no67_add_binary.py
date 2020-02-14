def add(b1, b2):
    b1r = b1[::-1]
    b2r = b2[::-1]
    n = max([len(b1), len(b2)])
    result = ['0' for x in range(n + 1)]

    carry = False

    for i in range(n + 1):
        b1t = '0'
        b2t = '0'

        if i < len(b1):
            b1t = b1r[i]

        if i < len(b2):
            b2t = b2r[i]

        sum = ord(b1t) - ord('0') + ord(b2t) - ord('0')
        
        if carry:
            sum += 1
            carry = False
        
        result[i] = chr(48 + (sum % 2))

        carry = sum >= 2
    
    return ''.join(result)
        

def main():
    print(add("00", "1"))
    print(add("1010", "1011"))


if __name__ == '__main__':
    main()