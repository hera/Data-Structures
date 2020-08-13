"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop()
"""

class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self, *argv):
        self.head = None
        self.tail = None
        self.length = 0

        # fill stack with elements
        for i in argv:
            self.push(i)

    def __str__(self):
        elements = []

        pointer = self.tail

        # follow every 'prev' link until reach None
        while pointer:
            elements.append(pointer.data)
            pointer = pointer.prev

        elements.reverse()

        result = ", ".join(str(e) for e in elements)

        return "Stack(%s)" % (result)
    
    def __len__(self):
        return self.length

    def len(self):
        return self.__len__()

    def push(self, data):
        # if stack is empty, head and tail point to the same node
        if self.head == None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            # stack has at least one element, so add a new node at the end
            self.tail = Node(data, self.tail)
        
        self.length += 1
    
    def pop(self):
        # in case stack is empty
        if self.head == None:
            return None
        
        popped = self.tail

        # in case there's only one element in stack
        if self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev

        self.length -= 1

        return popped.data