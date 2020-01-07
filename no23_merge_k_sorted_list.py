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


def merge(lists):
    
    done = False
    merged = None
    current = None
    temp = lists

    while not done:        
        buf = temp
        
        min_index = min(buf)

        if min_index == -1:
            break

        if merged is None:
            merged = temp[min_index]
        else:
            current.next = temp[min_index]
    
        current = temp[min_index]

        temp[min_index] = temp[min_index].next    

    return merged


def min(list):    
    min_index = -1

    for i in range(len(list)):
        if list[i] is not None:
            min_index = i
            break

    for i in range(1, len(list)):
        if list[i] is not None and list[i].val < list[min_index].val:            
            min_index = i
    
    return min_index


def main():
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    list3 = ListNode(2)
    list3.next = ListNode(6)

    result = merge([list1, list2, list3])
    print(result.print_all())


if __name__ == '__main__':
    main()