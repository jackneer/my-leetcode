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


def remove_nth_node_from_end(list, n):
    temp = []
    a = list

    while a is not None:
        temp.append(a)
        a = a.next

    temp[len(temp) - (n + 1)].next = temp[len(temp) - n].next
    temp[len(temp) - n] = None

    return list
    

def main():
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)
    
    result = remove_nth_node_from_end(list, 2)
    print(result.print_all())


if __name__ == '__main__':
    main()