##### heap_sort_ID.py

class Solution(object):
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
