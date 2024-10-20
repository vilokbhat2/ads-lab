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

    def reverseList(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev and current one step forward
            current = next_node
        self.head = prev  # Update the head to the new front of the list

def main():
    # Create a linked list
    my_list = SingleList()
    for value in [10, 20, 30, 40, 50]:
        my_list.addAtTail(value)

    print("Original Linked List:")
    my_list.printList()  # Expected output: 10 20 30 40 50

    # Reverse the linked list
    my_list.reverseList()
    print("Reversed Linked List:")
    my_list.printList()  # Expected output: 50 40 30 20 10

if __name__ == "__main__":
    main()
