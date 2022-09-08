from Node import Node

class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node 

        self.size += 1

    def pop(self):

        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else: 
                self.top = None

            return data
        else:
            print("Stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "Stack is empty"

        
    def clear(self):
        while self.top:
            self.pop()
        
    def find(self, value):
        data = self.top
        while data:
            if data.data == value:
                return True
            else:
                data = data.next
        
        return False