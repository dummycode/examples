class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        
        while i < length - 1:
            if (nums[i] != nums[i + 1]):
                return nums[i]
            i += 2
            
        return nums[length - 1]
        
