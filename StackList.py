"""
Implement stack using python list.
"""
class ListStack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        return self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack[-1]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack

# Create a stack
liststack = ListStack()
print(f"Stack is: {liststack.display()}")
liststack.push(10)
print(f"Stack is: {liststack.display()}")
liststack.push(20)
print(f"Stack is: {liststack.display()}")
liststack.push(30)
print(f"Stack is: {liststack.display()}")
liststack.push(40)
print(f"Stack is: {liststack.display()}")

liststack.pop()
print(f"Stack is: {liststack.display()}")
liststack.pop()
print(f"Stack is: {liststack.display()}")

print(f"Stack top is: {liststack.top()}")

print(f"Stack size is: {liststack.size()}")
print(f"Check stack is empty: {liststack.is_empty()}")
print(f"Stack is: {liststack.display()}")