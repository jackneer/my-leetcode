class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print_all(self):
        s = ''
        s += str(self.val)

        if self.next is not None:
            s += '->' + self.next.print_all()
        
        return s


def rotate(list, k):
    buf = []
    temp = list

    while temp is not None:
        buf.append(temp)
        temp = temp.next

    for i in range(k):
        buf[len(buf) - i - 2].next = None
        buf[len(buf) - i - 1].next = list
        list =   buf[len(buf) - i - 1]

    return list
    

def main():
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)
    
    result = rotate(list, 2)
    print(result.print_all())


if __name__ == '__main__':
    main()