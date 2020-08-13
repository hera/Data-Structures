class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, *argv):
        self.head = None
        self.tail = None
    
    def __str__(self):
        elements = []

        pointer = self.head

        # follow every 'next' link until reach None
        while pointer:
            elements.append(pointer.value)
            pointer = pointer.next

        result = ", ".join(str(e) for e in elements)

        return f"LinkedList({result})"
    
    def add_to_tail(self, value):
        # in case a queue is empty
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            # if queue has at least 1 element
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def remove_tail(self):
        # if list is empty
        if self.tail == None:
            return None
        
        # if only one item in the list
        if self.head == self.tail:
            removed_item = self.tail

            self.head = None
            self.tail = None

            return removed_item.value
        
        # save it for later
        removed_item = self.tail

        current = self.head

        # find the last but one
        while current.next != self.tail:
            current = current.next
        
        self.tail = current
        self.tail.next = None

        return removed_item.value

    def remove_head(self):
        if self.head == None:
            return None

        removed_item = self.head

        if self.head.next:
            self.head = self.head.next
        else:
            # that was the last item, the list is empty
            self.head = None
            self.tail = None

        return removed_item.value
    
    def contains(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        
        return False
