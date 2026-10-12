"""
    Binary Tree is non-linear data structure, where each node can have maximum of two children.
    Node with no child.
    Node with Left child.
    Node with Right child.
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None # Left child
        self.right = None # Right child

RootNode = BinaryTreeNode("A")
RootNode.left = BinaryTreeNode("B")
RootNode.right = BinaryTreeNode("C")
RootNode.left.left = BinaryTreeNode("D")

print(f"Root Node: {RootNode.data}")
print(f"Root's Left Node: {RootNode.left.data}")
print(f"Root's Right Node: {RootNode.right.data}")
print(f"Root's Left -> Left Node: {RootNode.left.left.data}")

# OUTPUT
#Root Node: A
#Root's Left Node: B
#Root's Right Node: C
#Root's Left -> Left Node: D

"""Supported operations
1. Insert item to Tree.
2. Delete item from Tree.
3. Search item in Tree.
4. Traverse the Tree.
    Pre-order: (Root --> Left --> Right)
    In-order : (Left --> Root --> Right)
    Post-order:(Left --> Right --> Root)
"""
# Using Recursion
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        if root is None:
            self.root = TreeNode(root)
        else:
            self.root = None

    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

Root = TreeNode(10)
Root.left = TreeNode(20)
Root.right = TreeNode(30)

bin_tree = BinaryTree(Root)
print("Pre-order traversal")
bin_tree.pre_order(Root)
print()
print("In-order traversal")
bin_tree.in_order(Root)
print()
print("Post-order traversal")
bin_tree.post_order(Root)

#OUTPUT
#Pre-order traversal
#10 20 30 
#In-order traversal
#20 10 30 
#Post-order traversal
#20 30 10 

#If not recursion we should use the explicit stack to keep track of the nodes we need to visit.