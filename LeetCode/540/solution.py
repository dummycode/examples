class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = int((l + r)/ 2)
            
            mid = mid if (mid % 2 == 0) else mid - 1 
            
            if (nums[mid] == nums[mid + 1]):
                # On right
                l = mid + 2
            else:
                # On left
                r = mid
            
        return nums[l]
        
