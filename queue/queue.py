"""
A queue is a value structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

"""

class Queue:
    def __init__(self, *argv):
        self.data = []

        self.data.extend(argv)

    def __str__(self):
        result = ", ".join(str(e) for e in self.data)
        return f"Queue({result})"

    def __len__(self):
        return len(self.data)

    def len(self):
        return self.__len__()
    
    def enqueue(self, data):
        self.data.append(data)
    
    def dequeue(self):
        if self.len() == 0:
            return None
        
        return self.data.pop(0)

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self, *argv):
        self.head = None
        self.tail = None
        self.length = 0

        for i in argv:
            self.enqueue(i)

    def __str__(self):
        elements = []

        pointer = self.head

        # follow every 'next' link until reach None
        while pointer:
            elements.append(pointer.value)
            pointer = pointer.next

        result = ", ".join(str(e) for e in elements)

        return f"Queue({result})"

    def __len__(self):
        return self.length

    def len(self):
        return self.__len__()
    
    def enqueue(self, value):
        # in case a queue is empty
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            # if queue has at least 1 element
            self.tail.next = Node(value)
            self.tail = self.tail.next
        
        self.length += 1

    def dequeue(self):
        if self.head == None:
            return None

        dequeued_item = self.head

        if self.head.next:
            self.head = self.head.next
        else:
            # that was the last item, the queue is empty now
            self.head = None
            self.tail = None
        
        self.length -= 1

        return dequeued_item.value