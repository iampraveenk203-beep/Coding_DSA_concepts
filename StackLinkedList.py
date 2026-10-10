"""
Implement stack using linked list.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, data):
        new_node = Node(data)
        # Insert node at the end
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        temp = self.top
        self.top = self.top.next
        self._size -= 1
        return temp.data
    
    def top_item(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.top.data
    
    def is_empty(self):
        if self.top is None:
            return True
        return False
    
    def size(self):
        return self._size
    
    def display(self):
        current = self.top
        stack = []
        while current:
            stack.append(str(current.data))
            current = current.next
        print("Top ->"+"->".join(stack) + "->None" if stack else "Stack is Empty")

stack = LinkedListStack()
stack.display()

stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.push(40)
stack.display()

print(f"Stack size is: {stack.size()}")
print(f"Stack TOP is: {stack.top_item()}")

stack.pop()
stack.display()
stack.pop()
stack.display()

print(f"Stack size is: {stack.size()}")

print(f"Stack is empty: {stack.is_empty()}")
stack.display()

