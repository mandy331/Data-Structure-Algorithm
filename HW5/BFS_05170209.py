from collections import defaultdict 

class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def IsEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def getSize(self):
        return len(self.stack)
        
class Queue:

    def __init__(self):
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        self.array.pop(0)
        
    def getFront(self) -> int:
        return self.array[0]
    
    def getBack(self):
        return self.array[-1]
        
    def IsEmpty(self) -> bool:
        if len(self.array) == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.array)
        
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        Queue1, Queue2 = Queue(), Queue() 
        start = s
        for k in range(len(self.graph)): 
            Queue2.push(start) 
            for i in self.graph[start]: 
                if (i not in Queue1.array) and (i not in Queue2.array):
                    Queue1.push(i) 
            if len(Queue1.array) != 0:
                start = Queue1.array[0] 
                Queue1.pop() 
            else:
                break
        return Queue2.array
        
    def DFS(self, s):
        Stack1 = Stack() 
        array_DFS = [] 
        start = s
        for k in range(len(self.graph)):
            array_DFS.append(start)
            for i in self.graph[start]:
                if (i not in Stack1.stack) and (i not in array_DFS):
                    Stack1.push(i) 
            if len(Stack1.stack) != 0:
                start = Stack1.top()
                Stack1.pop() 
            else:
                break       
        return array_DFS
        