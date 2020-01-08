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


    for i in range(n):
        temp.append(current)
        current = current.next
        
    print(temp)

    next = None
    for i in reversed(range(n)):
        if i == n -1:
            next = temp[i].next
            temp[i].next = temp[i - 1]
            list = temp[i]
        elif i == 0:
            temp[i].next = next
        else:
            temp[i].next = temp[i - 1]

        print(temp[i])

    return list


def main():
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)

    result = reverse(list, 3)
    print(result.print_all())


if __name__ == '__main__':
    main()