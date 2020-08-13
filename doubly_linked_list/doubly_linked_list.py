class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)
            

class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to 
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.value)
            current = current.next
        
        result = ", ".join(str(e) for e in elements)
        return f"DoublyLinkedList({result})"

    def truncate(self):
        """Make DoublyLinkedList instance empty"""

        self.head = None
        self.tail = None
        self.length = 0
    
    
    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        """

        # if list is empty
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
        elif self.head == self.tail:
            # there's only one element in the list
            self.head = ListNode(value, next=self.tail)
            self.tail.prev = self.head
        else:
            # there's at least 2 elements in the list
            new_node = ListNode(value, next=self.head)
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        
    
    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """

        if self.head == None:
            return None
        elif self.head == self.tail:
            deleted_element = self.head

            self.head = None
            self.tail = None
        else:
            deleted_element = self.head
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return deleted_element.value
            
    
    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        """

        # if list is empty
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            new_node = ListNode(value, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
            
    
    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        if self.tail == None:
            return None
        elif self.head == self.tail:
            deleted_element = self.tail
            self.truncate()
        else:
            deleted_element = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        return deleted_element.value

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """

        self.delete(node)
        self.add_to_head(node.value)
        
    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """

        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        """
        Deletes the input node from the List,
        preserving the order of the other elements of the List.
        """

        if self.length == 0:
            return None
        elif self.length == 1 and self.head == node:
            self.truncate()
        elif self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        
        return node.value

    def get_max(self):
        """Finds and returns the maximum value of all the nodes in the List."""

        num_list = []

        current = self.head

        while current:
            if type(current.value) == int or type(current.value) == float:
                num_list.append(current.value)
            current = current.next
        
        if len(num_list):
            return max(num_list)
