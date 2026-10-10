"""
Implement stack using python deque.
"""
from collections import deque

class DequeStack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def top_item(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def display(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack

stack = DequeStack()
print(f"Stack is: {stack.display()}")

stack.push(10)
print(f"Stack is: {stack.display()}")
stack.push(20)
print(f"Stack is: {stack.display()}")
stack.push(30)
print(f"Stack is: {stack.display()}")
stack.push(40)
print(f"Stack is: {stack.display()}")
print(f"Stack top item is: {stack.top_item()}")
stack.pop()
print(f"Stack is: {stack.display()}")
stack.pop()
print(f"Stack is: {stack.display()}")
stack.pop()
print(f"Stack is: {stack.display()}")
print(f"Stack top item is: {stack.top_item()}")

print(f"Stack is empty: {stack.is_empty()}")
print(f"Stack size: {stack.size()}")
