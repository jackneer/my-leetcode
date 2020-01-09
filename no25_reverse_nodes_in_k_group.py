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


def reverse(list, n):
    temp = []
    current = list
    prev = None
    head = None    

    while True:
        for i in range(n):
            if current is not None:
                temp.append(current)
                current = current.next
            else:
                break
        
        if len(temp) != n:
            break

        next = None

        if prev is not None:
            prev.next = temp[n - 1]

        for i in reversed(range(n)):
            if i == n -1:
                next = temp[i].next
                temp[i].next = temp[i - 1]
                if head is None:
                    head = temp[i]
            elif i == 0:
                temp[i].next = next
                
                prev = temp[i]
            else:
                temp[i].next = temp[i - 1]        
        
        temp = []

    return head


def main():
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)

    list = reverse(list, 2)
    print(list.print_all())
    # restore list
    list = reverse(list, 2)
    list = reverse(list, 3)
    print(list.print_all())


if __name__ == '__main__':
    main()