class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        self.nums = nums
        if len(self.nums) > 1:
            mid = (len(self.nums)) //2 
            left_array = self.nums[:mid]
            right_array = self.nums[mid:]    
            self.merge_sort(left_array)
            self.merge_sort(right_array)
            self.merge(left_array, right_array)
        return self.nums

    def merge(self, left, right):
        size = len(left) + len(right)
        tmp = [0] * size

        i = j = k = 0
        while (i < len(left)) and (j < len(right)): 
            if left[i] <= right[j]:
                tmp[k] = left[i]
                i = i + 1
            elif left[i] > right[j]:
                tmp[k] = right[j]
                j = j + 1
            k = k + 1

        while j < len(right): # i >= len(left) and 
            tmp[k] = right[j]
            j = j + 1
            k = k + 1

        while i < len(left): # j >= len(right) and
            tmp[k] = left[i]
            i = i + 1
            k = k + 1
        
        return tmp
