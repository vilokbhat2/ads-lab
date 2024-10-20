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

    def findMiddle(self):
        if self.isEmpty():
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def main():
    # Create a linked list
    my_list = SingleList()
    for value in [10, 20, 30, 40, 50]:
        my_list.addAtTail(value)

    print("Linked List:")
    my_list.printList()  # Expected output: 10 20 30 40 50

    # Find the middle element
    middle_node = my_list.findMiddle()
    if middle_node:
        print("Middle Element:", middle_node.data)  # Expected output: 30
    else:
        print("The list is empty.")

    # Test with an even number of elements
    even_list = SingleList()
    for value in [1, 2, 3, 4]:
        even_list.addAtTail(value)

    print("Even List:")
    even_list.printList()  # Expected output: 1 2 3 4

    # Find the middle element of the even list
    middle_node = even_list.findMiddle()
    if middle_node:
        print("Middle Element:", middle_node.data)  # Expected output: 3 (second of the two middle elements)
    else:
        print("The list is empty.")


if __name__ == "__main__":
    main()
