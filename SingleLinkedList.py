from this import d
from Node import Node

class SingleLinkedList():

    def __init__(self):
        self.tail = None
        self.head = self
        self.len = 0

    def append(self, data):
        node = Node(data)

        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            
            while current.next:
                current = current.next
            
            current.next = node

        self.len += 1

    def size(self):
        return self.len

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail
        
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

                previous = current
                current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')

    def clean(self):
        self.tail = None
        self.head = None
        self.size = 0