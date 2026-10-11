"""
   | Data  |  Next | ----> | Data | Next | ---> None
   Is linear data structure to store the data.
   Each node has Data and Next pointer, Next pointer points to next node.
   Last node next pointer points to None.
   First is always a points to head.
   If linked list is empty then head point to None.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None
    
    def insert_at_begining(self, data):
        # Create a new node
        new_node = Node(data)
        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
        else:
            # Case 2: When list has items
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        # Create new node
        new_node = Node(data)
        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
        else:
            # Case 2: List has items and traverse the list using current.
            current = self.head
            while current.next is not None:
                current = current.next
            # Case 3: Link the last node (current) to new_node.
            current.next = new_node
    
    def insert_by_pos(self, data, pos):
        # Create new node
        new_node = Node(data)

        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
        else:
            # Case 2: pos is 0, insert at the begining
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                # Case 3: List has items and pos is non-zero
                # Traverse the list till pos-1
                current = self.head
                count = 0
                while current and count < pos - 1:
                    current = current.next
                    count += 1
                # Case 4: Check current is reached end node
                if current is None:
                    print(f"List is out of range")
                # Case 4: Link the current node to new_node
                new_node.next = current.next
                current.next = new_node
    
    def display(self):
        # Case 1: List is empty
        if self.head is None:
            print(f"LinkedList is empty")
        # Case 2: Traverse the list
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print("->".join(items))
            

    def delete_begining(self):
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")
            return
        # Case 2: List has only node
        if self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            # Case 3: List has more than one node.
            temp = self.head.data
            self.head = self.head.next
            return temp
    
    def delete_at_end(self):
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")
            return
        # Case 2: List has only node
        if self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            # Case 3: Traverse the list till last but one node.
            current = self.head
            while current.next.next is not None:
                current = current.next
            # Case 4: Save the value of node.
            temp = current.next.data

            # Case 5: Break the link
            current.next = None
            return temp
    
    def delete_by_pos(self, pos):
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")
            return
        # Case 2: pos is 0
        if pos == 0:
            temp = self.head.data
            self.head = self.head.next
            return temp
        else:
            # Case 3: Traverse the list till pos - 1
            count = 0
            current = self.head
            while current and count < pos - 1:
                current = current.next
            # Case 4: current already reached last node
            if current is None or current.next is None:
                print(f"Pos is out of range")
                return
            else:
                # Case 5: Unlink the pos node from current node and point to the pos next node
                temp = current.next.data
                current.next = current.next.next
                return temp

ll = LinkedList()
ll.insert_at_begining(1)
ll.display()
ll.insert_at_end(2)
ll.display()
ll.insert_at_end(3)
ll.display()
ll.insert_by_pos(20,2)
ll.display()

ll.delete_begining()
ll.display()
ll.delete_at_end()
ll.display()
ll.delete_by_pos(1)
ll.display()

