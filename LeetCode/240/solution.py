class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: 
            return False
        
        r, c = 0, len(matrix[0]) - 1
        
        while True:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
            
            if r >= len(matrix) or c < 0:
                return False
        
