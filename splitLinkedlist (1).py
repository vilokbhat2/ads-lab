class SingleList:
    class _Node_:
        def __init__(self, ele):
            self.data = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def addAtTail(self, ele):
        newNode = self._Node_(ele)
        if not self.isEmpty():
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
        self.count += 1

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def split(self):
        list1 = SingleList()
        list2 = SingleList()

        current = self.head
        turn = True  # Use this flag to alternate between list1 and list2

        while current:
            if turn:
                list1.addAtTail(current.data)
            else:
                list2.addAtTail(current.data)
            turn = not turn  # Toggle the turn flag
            current = current.next

        return list1, list2

def main():
    # Create a linked list
    my_list = SingleList()
    for value in [10, 20, 30, 40, 50, 60, 70]:
        my_list.addAtTail(value)

    print("Original Linked List:")
    my_list.printList()  # Expected output: 10 20 30 40 50 60 70

    # Split the list
    list1, list2 = my_list.split()

    print("List 1 after split:")
    list1.printList()  # Expected output: 10 30 50 70

    print("List 2 after split:")
    list2.printList()  # Expected output: 20 40 60

if __name__ == "__main__":
    main()
