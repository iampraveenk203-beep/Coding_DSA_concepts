"""
It is linear data structure to store the data
Each nodes next pointer points to the next node.
Head node is the first node of the list.
Last/tail node is always points back to head node.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.tail = None # Points to last node of circle.
    
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case 1: List is empty
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node # point to itself to create a circle.
            return
        # Case 2: List has items
        new_node.next = self.tail.next # link to new node
        self.tail.next = new_node # point to tail the new head
    
    def insert_at_end(self, data):
        new_node = Node(data)
        # Case 1: List is empty
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
            return
        # Case 2: List has items
        new_node.next = self.tail.next # link new node to the head
        self.tail.next = new_node # point old tail to new node
        self.tail = new_node # Update tail pointer
    
    def insert_by_pos(self, data, pos):
        new_node = Node(data)
        # Case 1: List is empty
        if self.tail is None:
            if pos == 0:
                self.tail = new_node
                new_node.next = new_node
            else:
                print(f"Pos is out of range")
            return
        # Case 2: Insert at pos = 0
        if pos == 0:
            new_node.next = self.tail.next
            self.tail.next = new_node
            return
        # Case 3: Insert at the middle or at the end
        # Traverse the circular list
        count = 0
        current = self.tail.next # Start with head

        while count < pos - 1:
            current = current.next
            count += 1
            # If we looped all the way back to head then pos is out of range.
            if current == self.tail.next:
                print("Pos is out of range")
        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node
    
    def display(self):
        # Case 1: list is empty.
        if self.tail is None:
            print("List is empty.")
            return
        # Case 2: List has the items
        # Traverse the list
        head = self.tail.next
        current = head
        items = []

        while True:
            items.append(str(current.data))
            current = current.next
            if current == head:
                break
        print("->".join(items)+"(Back to Start)")
    
    def delete_at_beginning(self):
        # Case 1: List is empty
        if self.tail is None:
            print("List is empty")
            return
        head = self.tail.next
        temp = head.data

        # Case 2: only one node.
        if self.tail == head:
            self.tail = None
        else:
            # Case 3: multiple node
            self.tail.next = head.next
        return temp
    
    def delete_at_end(self):
        # Case 1: List is empty
        if self.tail is None:
            print("List is empty")
            return
        head = self.tail.next
        temp = head.data
        # Case 2: List has only one node
        if self.tail == head:
            self.tail = None
        else:
            # Case 3: multiple nodes
            # Traverse the list till second last node
            current = head
            while current.next != self.tail:
                current = current.next
            current.next = head # link last but one node to head node
            self.tail = current # update tail node
    
    def delete_by_value(self, value):
        # Case 1: list is empty
        if self.tail is None:
            print("List is empty")
            return
        
        head = self.tail.next
        current = head
        prev = self.tail

        # Case 2: Traverse the list
        while True:
            if current.data == value:
                # Case 3: only one node
                if current == prev:
                    self.tail = None
                    return True
                # Case 4: Deleting the head node
                if current == head:
                    self.tail.next = head.next
                    return True
                # Case 5: Deleting tail node
                if current == self.tail:
                    prev.next = head
                    self.tail = prev
                    return True
                # Case 6: Deleting intermediate node
                prev.next = current.next
                return True
            prev = current
            current = current.next
            if current == head:
                print("Given value is not found in list")
                break
        return False

cl = CircularList()
cl.insert_at_beginning(1)
cl.insert_at_beginning(2)
cl.display()
cl.insert_at_end(3)
cl.insert_at_end(5)
cl.display()
cl.insert_by_pos(1,4)
cl.display()
cl.delete_at_beginning()
cl.display()
cl.delete_at_end()
cl.display()
cl.delete_by_value(4)
cl.display()

""" OUTPUT:
2->1(Back to Start)
2->1->3->5(Back to Start)
2->1->3->5->1(Back to Start)
1->3->5->1(Back to Start)
1->3->5(Back to Start)
Given value is not found in list
1->3->5(Back to Start)"""