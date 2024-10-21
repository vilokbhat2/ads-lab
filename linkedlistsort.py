class Node:
    def __init__(self, reg_no, program, cgpa):
        self.reg_no = reg_no
        self.program = program
        self.cgpa = cgpa
        self.next = None

def sort_linked_list(head):
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    # Recursively sort the two halves
    left = sort_linked_list(head)
    right = sort_linked_list(second_half)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.cgpa <= right.cgpa:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

# Example usage
# Create the linked list
head = Node(1, "Computer Science", 3.5)
node2 = Node(2, "Electrical Engineering", 3.2)
node3 = Node(3, "Mechanical Engineering", 3.8)
node4 = Node(4, "Civil Engineering", 3.6)

head.next = node2
node2.next = node3
node3.next = node4

# Sort the linked list based on CGPA
head = sort_linked_list(head)

# Print the sorted linked list
current = head
while current:
    print(f"Reg No: {current.reg_no}, Program: {current.program}, CGPA: {current.cgpa}")
    current = current.next