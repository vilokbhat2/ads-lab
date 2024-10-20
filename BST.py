'''Design BST data structure and implement the following methods
a. Check BST is empty
b. Get count of nodes in BST
c. Add node to BST
d. Search node in BST
e. Tree traversal
i. In-order
ii. Pre-order
iii. Post-order
iv. Level-order
f. Delete specified node
g. Find height of BST
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def add_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_node(self.root, key)

    def _add_node(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add_node(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add_node(node.right, key)

    def search_node(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_node(node.left, key)
        return self._search_node(node.right, key)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val, end=' ')
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.val, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val, end=' ')

    def level_order_traversal(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def delete_node(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_node(node.left, key)
        elif key > node.val:
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_node(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_height(self, node):
        if node is None:
            return -1
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return 1 + max(left_height, right_height)

# Example usage:
bst = BST()
bst.add_node(50)
bst.add_node(30)
bst.add_node(20)
bst.add_node(40)
bst.add_node(70)
bst.add_node(60)
bst.add_node(80)

print("In-order traversal:")
bst.in_order_traversal(bst.root)
print("\nPre-order traversal:")
bst.pre_order_traversal(bst.root)
print("\nPost-order traversal:")
bst.post_order_traversal(bst.root)
print("\nLevel-order traversal:")
bst.level_order_traversal()

print("\n\nIs BST empty?", bst.is_empty())
print("Count of nodes:", bst.count_nodes(bst.root))
print("Search for node with value 40:", bst.search_node(40) is not None)
print("Height of BST:", bst.find_height(bst.root))

bst.delete_node(20)
print("\nIn-order traversal after deleting 20:")
bst.in_order_traversal(bst.root)