class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    node1 = l1
    node2 = l2
    digit = 0
    sum = 0

    while node1 is not None or node2 is not None:
        val1 = node1.val if node1 is not None else 0
        val2 = node2.val if node2 is not None else 0
        sum += (val1 + val2) * (10 ** digit)
        node1 = node1.next
        node2 = node2.next
        digit += 1

    return sum
    

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    sum = add_two_numbers(l1, l2)
    print(sum)


if __name__ == '__main__':
    main()