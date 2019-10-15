class Node:
    #單向Linked-list
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.length = 0

    def get(self, index):
        if index >= self.length or index < 0:
            return -1
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current.val
        
    def addAtHead(self, val):
        addhead = Node(val)
        if self.length == 0:
            self.head = addhead
            addhead.next = None
        else:
            addhead.next = self.head
            self.head = addhead
        self.length += 1
        
        

    def addAtTail(self, val):
        addtail = Node(val)
        if self.length == 0:
            self.head = addtail
            addtail.next = None
        else:
            current = self.head
            for i in range(self.length - 1):
                current = current.next
            current.next = addtail
        self.length += 1
        
    
    
    def addAtIndex(self, index, val):
        if index > self.length:
            pass

        elif self.length >= 1 and index == self.length:
            self.addAtTail(val)
            

        elif index <= 0:
            self.addAtHead(val)
            
        
        else:
            addindex = Node(val)
            current = self.head
            for i in range(index - 1):
                current = current.next
            addindex.next = current.next
            current.next = addindex
            self.length += 1

    def deleteAtIndex(self, index):
        if index >= self.length or index < 0:
            pass
        
        elif self.length >= 2 and index == self.length - 1:
            current = self.head
            for i in range(self.length - 2):
                current = current.next
            current.next = None
            self.length -= 1
  
            
        elif index == 0:
            if self.length == 1:
                self.head = None
            else:
                current = self.head
                self.head = current.next
            self.length -= 1
            

        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            self.length -= 1