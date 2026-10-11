"""
Implement Queue using python queue package.
"""
from queue import Queue

q = Queue(maxsize=4)

q.put(10)

q.put(20)

q.put(30)

q.put(40)

q.get()

q.get()

q.put(50)

q.put(60)
try:
    q.put(70, block=False)
except:
    print("Queue maxsize is reached.")


