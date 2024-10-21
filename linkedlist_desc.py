# Assume that you have one unsorted student linked list. Create sorted (based on CGPA) program wise single linked list based on CGPA in descending order.
class Node:
    def __init__(self, reg_no, program, cgpa):
        self.reg_no = reg_no
        self.program = program
        self.cgpa = cgpa
        self.next = None
        
def insertion_sort(head):
    sorted_list = None
    current = head
    while current:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node
    return sorted_list

def sorted_insert(sorted_list, new_node):
    if not sorted_list or sorted_list.cgpa < new_node.cgpa:
        new_node.next = sorted_list
        sorted_list = new_node
    else:
        current = sorted_list
        while current.next and current.next.cgpa >= new_node.cgpa:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_list

def print_list(node):
    while node:
        print(f'Reg No: {node.reg_no}, Program: {node.program}, CGPA: {node.cgpa}')
        node = node.next

head = Node(1, 'Program1', 3.2)
head.next = Node(2, 'Program1', 2.8)
head.next.next = Node(3, 'Program1', 3.5)
head.next.next.next = Node(4, 'Program2', 3.0)
head.next.next.next.next = Node(5, 'Program2', 3.7)
head.next.next.next.next.next = Node(6, 'Program2', 2.9)

sorted_head = insertion_sort(head)

print_list(sorted_head)