# Assume that you have two unsorted student linked lists (one for each program). Merge the nodes into one single list based on CGPA.
class Node:
    def __init__(self, reg_no, program, cgpa):
        self.reg_no = reg_no
        self.program = program
        self.cgpa = cgpa
        self.next = None
        
def merge_lists(list1, list2):
    dummy = Node(0, '', 0) # Dummy node to start the merge list
    tail = dummy
    while list1 and list2:
        if list1.cgpa <= list2.cgpa:
            tail.next = list1
            list1 = list1.next 
        else:
            tail.next = list2
            list2 = list2.next 
        tail = tail.next 
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next

def print_list(node):
    while node:
        print(f"{node.reg_no}, Program: {node.program}, CGPA: {node.cgpa}")
        node = node.next
        
list1 = Node(1, 'Program1', 3.2)
list1.next = Node(2, 'Program1', 2.8)
list1.next.next = Node(3, 'Program1', 3.5)

list2 = Node(4, 'Program2', 3.0)
list2.next = Node(5, 'Program2', 3.7)
list2.next.next = Node(6, 'Program2', 2.9)

merged_list = merge_lists(list1, list2)

print_list(merged_list)
