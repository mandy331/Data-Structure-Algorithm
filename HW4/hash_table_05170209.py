from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val = None):
        self.head = ListNode(val) 
        self.length = 0
    
    def addAtHead(self, val):
        addhead = ListNode(val)
        if self.length == 0:
            self.head = addhead
            addhead.next = None
        
        else:
            addhead.next = self.head
            self.head = addhead
        self.length += 1
        
    def addAtTail(self, val):
        addtail = ListNode(val)
        if self.length == 0: 
            self.head = addtail
            addtail.next = None
        
        else:
            current = self.head
            for i in range(self.length - 1): 
                current = current.next
            current.next = addtail
        self.length += 1
    
    def search_index(self, val):
        duplicated = []
        current = self.head
        for i in range(self.length):
            if current.val == val:
                duplicated.append(i)
            current = current.next
        return duplicated
    
    def delete(self, index): 
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
            

    def search(self, val):
        if self.length == 0 or self.head.val == None: 
            return False
        
        current = self.head 
        for i in range(self.length): 
            if current.val == val:
                return True
            current = current.next
        return False
    
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def MD5_Hash_Function(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h_10 = int(h.hexdigest(),16)
        return h_10 % self.capacity
        
    def add(self, key):
        cur_box = self.data[self.MD5_Hash_Function(key)] 
        if cur_box == None: 
            cur_box = LinkedList() 
            cur_box.addAtHead(key) 
        else: 
            cur_box.addAtTail(key) 
        self.data[self.MD5_Hash_Function(key)] = cur_box 
             
    def remove(self, key):
        cur_box = self.data[self.MD5_Hash_Function(key)] 
        if cur_box == None: 
            return 
        
        else: 
            duplicated = cur_box.search_index(key) 
            for i in range(len(duplicated)): 
                k = len(duplicated) - 1 - i 
                cur_box.delete(duplicated[k]) 
            
            if cur_box.length == 0: 
                cur_box = None
            
            self.data[self.MD5_Hash_Function(key)] = cur_box 
        
    def contains(self, key):
        cur_box = self.data[self.MD5_Hash_Function(key)] 
        if cur_box == None: 
            return False
        else: 
            return cur_box.search(key)