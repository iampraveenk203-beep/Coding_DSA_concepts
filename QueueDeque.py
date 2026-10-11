"""
Queue can be implemented using python list but:
    1. Python list are contigous memory so whenever first item removed from list then other items has to be shift to the left.
       enqueue: list.append()
       dequeue: list.pop(0)
So Python provides the below packages to implement the queue.
deque from collections package
queue from queue
"""
from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()
    
    def insert(self, item):
        self.queue.append(item)
    
    def remove(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()
    
    def size(self):
        return len(self.queue)
    
    def first_item(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue

q = QueueDeque()
q.insert(10)
print(f"Queue is: {q.display()}")
print(f"Queue first item: {q.first_item()}")
q.insert(20)
print(f"Queue is: {q.display()}")
q.insert(30)
print(f"Queue is: {q.display()}")
q.insert(40)
print(f"Queue is: {q.display()}")
q.insert(50)
print(f"Queue is: {q.display()}")
q.remove()
print(f"Queue is: {q.display()}")
q.remove()
print(f"Queue is: {q.display()}")
q.remove()
print(f"Queue is: {q.display()}")
print(f"Queue is empty: {q.is_empty()}")
print(f"Queue first item: {q.first_item()}")
print(f"Queue is: {q.display()}")

"""OUTPTUT
Queue is: deque([10, 20])
Queue is: deque([10, 20, 30])
Queue is: deque([10, 20, 30, 40])
Queue is: deque([10, 20, 30, 40, 50])
Queue is: deque([20, 30, 40, 50])
Queue is: deque([30, 40, 50])
Queue is: deque([40, 50])
Queue is empty: False
Queue first item: 40
Queue is: deque([40, 50])"""