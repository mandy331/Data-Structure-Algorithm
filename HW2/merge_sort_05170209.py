class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        self.array = nums
        self.start = 0
        self.end = len(nums)-1
        self.run(self.array, self.start, self.end)
        return self.array
        
    def run(self, array, start, end):
        if len(array) <= 1:
            return self.array
        if end - start >= 1:
            div = (start + end + 1) // 2 # 改成div，且要以該段待排序的list的長度來除以2
            self.run(array, start, div - 1) 
            self.run(array, div, end)
            self.merge(array, start, div, end)
        
    
    def merge(self, array, start, div, end):
        left = array[start : div]
        right = array[div : end + 1]
        
        i = j = 0
        k = start 

        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while (i < len(left)) and (j >= len(right)):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while (j < len(right)) and (i >= len(left)):
            array[k] = right[j]
            j = j + 1
            k = k + 1