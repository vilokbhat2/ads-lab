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
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def isPalindrome(self):
        if self.isEmpty() or self.head.next is None:
            return True

        # Find the middle of the list
        slow = self.head
        fast = self.head
        prev_of_slow = None

        while fast and fast.next:
            fast = fast.next.next
            prev_of_slow = slow
            slow = slow.next

        # For odd number of elements, move slow one step further
        second_half = None
        if fast:
            second_half = slow.next
        else:
            second_half = slow

        # Split the list into two halves
        if prev_of_slow:
            prev_of_slow.next = None

        # Reverse the second half
        second_half_reversed = SingleList()
        while second_half:
            second_half_reversed.addAtTail(second_half.data)
            second_half = second_half.next

        second_half_reversed.reverseList()
        second_half = second_half_reversed.head

        # Compare the two halves
        first_half = self.head
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

def main():
    # Create a linked list
    my_list = SingleList()
    for value in [1, 2, 3, 2, 1]:
        my_list.addAtTail(value)

    print("Linked List:")
    my_list.printList()  # Expected output: 1 2 3 2 1

    # Check if the list is a palindrome
    print("Is the linked list a palindrome?", my_list.isPalindrome())  # Expected output: True

    # Test with a non-palindrome list
    non_palindrome_list = SingleList()
    for value in [1, 2, 3, 4, 5]:
        non_palindrome_list.addAtTail(value)

    print("Non-Palindrome Linked List:")
    non_palindrome_list.printList()  # Expected output: 1 2 3 4 5

    print("Is the linked list a palindrome?", non_palindrome_list.isPalindrome())  # Expected output: False

if __name__ == "__main__":
    main()
