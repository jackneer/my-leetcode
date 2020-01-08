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


def pair_swap(list):
    current = list
    prev = None

    while current is not None:
        temp = current.next
        current.next = current.next.next
        temp.next = current                
        
        if prev is None:
            list = temp
        else:
            prev.next = temp

        prev = current
        current = current.next

    return list


def main():
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)

    result = pair_swap(list)
    print(result.print_all())


if __name__ == '__main__':
    main()