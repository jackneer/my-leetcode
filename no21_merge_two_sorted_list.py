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


def merge(list1, list2):
    a = list1
    b = list2
    merged = None
    current = None
    
    while a is not None and b is not None:
        temp = None
        if a.val <= b.val:
            temp = a
            a = a.next
        else:
            temp = b
            b = b.next

        if merged is None:
            merged = temp
        else:
            current.next = temp
        
        current = temp
    
    if a is not None:
        current.next = a
    
    if b is not None:
        current.next = b

    return merged
    

def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    result = merge(list1, list2)
    print(result.print_all())


if __name__ == '__main__':
    main()