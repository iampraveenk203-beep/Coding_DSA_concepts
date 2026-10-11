"""
In this list each node will have two pointers 

| Left | Data | Right|

It is linear data structure to store the data.
Each nodes right pointer points to next mode.
Each nodes left pointer points back to prev node.
First node is the head node and first node left pointer is always None.
Last node is the tail node and last node rifht pointer is always None.
"""
class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case 1: Link new node
        new_node.next = self.head

        # Case 2: If head is not None then link head.prev to new_node.
        if self.head is not None:
            self.head.prev = new_node
        
        # Case 3: update the head pointer
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)

        # Case 1: If list is emmpty
        if self.head is None:
            self.head = new_node
        else:
            # Case 2: Traverse the list till last node.
            current = self.head
            while current.next is not None:
                current = current.next
            
            # Case 3: Link new node at the end.
            current.next = new_node
            new_node.prv = current
    
    def insert_by_pos(self, pos, data):
        new_node = Node(data)

        # Case 1: If pos = 0 insert at begining
        if pos == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        
        # Case 2: Traverse the list till pos - 1
        current = self.head
        count = 0
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Pos is out of range")
        else:
            # Case 3: Link new_node after the pos.
            new_node.next = current.next
            new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
    
    def display(self):
        # Case 1: List is empty
        if self.head is None:
            print(f"List is empty.")
        # Case 2: Traverse the list and collect the items.
        items = []
        current = self.head
        while current.next is not None:
            items.append(str(current.data))
            current = current.next
        print("<-->".join(items) if items else 'Doubly linked list is empty')
    
    def delete_at_beginning(self):
        # Case 1: List is empty
        if self.head is None:
            print("Doubly linked list is empty")
        
        # Case 2: Store the data of node to temp (being deleted)
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp.data
    
    def delete_at_end(self):
        # Case 1: List is empty
        if self.head is None:
            print(f"Doubly linked list is empty.")
        else:
            # Case 2: List has only node
            temp = None
            if self.head.next is None:
                temp = self.head
                self.head = None
                return temp.data
            else:
                # Case 3: Traverse the list till last but one node.
                current = self.head
                while current.next.next is not None:
                    current = current.next
                temp = current.next.data
                # Case 4: Unlink the current node from last but one node.
                current.next = None
                return temp
    
    def delete_by_pos(self, pos):
        # Case 1: list is empty
        if self.head is None:
            print(f"List is empty")
        else:
            # Case 2: Traverse the list untill reach pos - 1
            current = self.head
            count = 0
            temp = None
            while current.next is not None and count < pos - 1:
                current = current.next
            if current.next is None:
                print(f"Pos is out of range")
            else:
                temp = current.next.data
                if current.next.next is not None:
                    current.next = current.next.next
                if current.next.next.prev is not None:
                    current.next.next.prev = current
                return temp
    
    def delete_by_value(self, value):
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")

        # Traverse the list to match the given value
        current = self.head

        while current is not None:
            if current.data == value:
                # Case 2 The node to delete is the Head node
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                    return True
                # Case 3 The node is to delete is middle or tail
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
            current = current.next

dl = DoubleLinkedList()
dl.insert_at_beginning(1)
dl.insert_at_beginning(2)
dl.insert_at_beginning(3)
dl.display()
dl.insert_at_end(3)
dl.display()
dl.insert_by_pos(2,5)
dl.display()
dl.delete_at_beginning()
dl.display()
dl.delete_at_end()
dl.display()
dl.delete_by_value(5)
dl.display()
dl.delete_by_pos(2)     
dl.display() 

        
