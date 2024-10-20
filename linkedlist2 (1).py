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

    def listCount(self):
        return self.count

    def addAtHead(self, ele):
        newNode = self._Node_(ele)
        if not self.isEmpty():
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = self.tail = newNode
        self.count += 1

    def addAtTail(self, ele):
        newNode = self._Node_(ele)
        if not self.isEmpty():
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
        self.count += 1

    def isMember(self, key):
        if not self.isEmpty():
            cur = self.head
            while cur is not None:
                if cur.data == key:
                    return True
                cur = cur.next
        return False

    def delheadNode(self):
        if not self.isEmpty():
            ele = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return ele
        return None

    def delTailNode(self):
        if not self.isEmpty():
            ele = self.tail.data
            if self.count == 1:
                self.head = self.tail = None
            else:
                cur = self.head
                while cur.next != self.tail:
                    cur = cur.next
                cur.next = None
                self.tail = cur
            self.count -= 1
            return ele
        return None

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def createCommonList(list1, list2):
    common_list = SingleList()
    # Use a set to store elements of the first list for fast lookup
    elements_set = set()

    current = list1.head
    while current:
        elements_set.add(current.data)
        current = current.next

    # Traverse the second list and add common elements to the common list
    current = list2.head
    while current:
        if current.data in elements_set:
            common_list.addAtTail(current.data)
        current = current.next

    return common_list


def main():
    # Create two linked lists with some common elements
    list1 = SingleList()
    list2 = SingleList()

    # Add elements to the first list
    list1.addAtHead(10)
    list1.addAtHead(20)
    list1.addAtHead(30)
    list1.addAtHead(40)
    print("List 1:")
    list1.printList()  # Expected output: 40 30 20 10

    # Add elements to the second list
    list2.addAtHead(15)
    list2.addAtHead(30)
    list2.addAtHead(20)
    list2.addAtHead(5)
    print("List 2:")
    list2.printList()  # Expected output: 5 20 30 15

    # Create a third list with common elements
    common_list = createCommonList(list1, list2)
    print("Common List:")
    common_list.printList()  # Expected output: 20 30


if __name__ == "__main__":
    main()
