"""
Binary Search Tree: To build a binary tree that allows for efficient insert, 
                    delete and search we use BST (Binary Search Tree).
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, current_node, data):
        # Case 1: data < current_node.data
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursively(current_node.left, data)
        # Case 2: data > current_node.data
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursively(current_node.right, data)

        # If data == current_node.data, do nothing (duplicates not allowed)

    def search(self, data):
        # Case 1: Check Tree is empty
        if self.root is None:
            print("BST is empty")
        else:
            # Case 2: Search the data in tree by traversing the tree.
            return self._search_recursively(self.root, data)

    def _search_recursively(self, current_node, data):
        # Case 1: Root is null or BST is empty
        if current_node is None:
            return False
        # Case 2: data is equal to current node data
        if current_node.data == data:
            return True
        # Case 3: data < current node data
        if data < current_node.data:
            return self._search_recursively(current_node.left, data)
        # Case 4: data > current node data
        elif data > current_node.data:
            return self._search_recursively(current_node.right, data)

    # Get the nodes in sorted order (Left -> Root --> Right)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        # Case 1: If node exists then call recursion method in order (Left -> Root -> Right)
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.data)
            self._inorder_recursive(current_node.right, result)

    def find_min(self):
        # Case 1: Tree is empty
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, current_node):
        # Case 1: Tree is empty
        if current_node is None:
            return None
        # Case 2: If node does not have left child
        elif current_node.left is None:
            return current_node.data
        # Case 3: If node has left child
        else:
            return self._find_min(current_node.left)

    def find_max(self):
        # Case 1: Tree is empty
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, current_node):
        # Case 1: Node is empty
        if current_node is None:
            return None
        # Case 2: If node does not have right child
        elif current_node.right is None:
            return current_node.data
        # Case 3: If node has right child
        else:
            return self._find_max(current_node.right)

bst_tree = BST()
bst_tree.insert(50)
bst_tree.insert(20)
bst_tree.insert(30)
bst_tree.insert(70)
bst_tree.insert(80)
print(f"Traverse the list in-order: {bst_tree.inorder_traversal()}")
print(f"Search item 30: {bst_tree.search(30)}")
print(f"Minimum node is: {bst_tree.find_min()}")
print(f"Maximum node is: {bst_tree.find_max()}")

# OUTPUT
#Traverse the list in-order: [20, 30, 50, 70, 80]
#Search item 30: True
#Minimum node is: 20
#Minimum node is: 80