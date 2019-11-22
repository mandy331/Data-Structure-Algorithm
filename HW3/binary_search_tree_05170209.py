# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def __init__(self):
        self.root = None
    
    def add_root(self, val):
        self.root = TreeNode(val)
    
    def preorder_array(self, start, array): 
        if type(array) == list:
            if start:
                array.append(start.val)
                self.preorder_array(start.left, array)
                self.preorder_array(start.right, array)
            return array
        
    def insertNode(self, Current, val):  
        if val <= Current.val:
            if Current.left:
                return self.insertNode(Current.left, val)
            else:
                Current.left = TreeNode(val) 
                return Current.left
        else:
            if Current.right:
                return self.insertNode(Current.right, val)
            else:
                Current.right = TreeNode(val)
                return Current.right
    
    def heap_sort(self, nums):
        self.array = nums
        self.heapsize = len(nums)
        self.BuildMaxHeap(self.array)
        for i in range(len(self.array) - 1):
            heaplast = (len(self.array) - 1) - i
            self.array[0], self.array[heaplast] = self.array[heaplast], self.array[0]
            self.heapsize = self.heapsize - 1
            self.Heapify(self.array,0)
        return self.array

    def BuildMaxHeap(self, array): 
        n = self.heapsize
        for j in range(n//2 + 1):
            i = n//2 - j        
            self.Heapify(self.array, i)

    def Heapify(self, array, i):
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= self.heapsize - 1 and self.array[left] > self.array[i]:
            Max = left
        else:
            Max = i
        if right <= self.heapsize - 1 and self.array[right] > self.array[Max]:
            Max = right
        if Max != i:
            self.array[i], self.array[Max] = self.array[Max], self.array[i]
            self.Heapify(self.array, Max)
    
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if self.root is None:
            self.root = root
            return self.insertNode(self.root, val)
        else:
            return self.insertNode(root, val)

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        old_array = self.preorder_array(root, [])
        new_array = [i for i in old_array if i != target]
        
        new_sort_array = self.heap_sort(new_array)
        root_index = len(new_sort_array) // 2
        self.add_root(new_sort_array[root_index])

        for k in range(len(new_sort_array)):
            if k != root_index:
                self.insert(self.root, new_sort_array[k])
        return self.root
        
        
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root is None:
            return None
        
        else:
            if target == root.val: 
                return root

            if target <= root.val: 
                return self.search(root.left, target)

            else:
                return self.search(root.right, target)
        
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        old_array = self.preorder_array(root, [])
        new_array = []
        for i in old_array:
            if i == target:
                i = new_val
                new_array.append(i)
            else:
                new_array.append(i)
        
        new_sort_array = self.heap_sort(new_array)
        root_index = len(new_sort_array)//2
        self.add_root(new_sort_array[root_index])
        
        for k in range(len(new_sort_array)):
            if k != root_index:
                self.insert(self.root, new_sort_array[k])
        return self.root
        
        