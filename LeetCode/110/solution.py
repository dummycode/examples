class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balanced_helper(root)[1]
        
    def balanced_helper(self, root):
        if (root == None):
            return (-1, True)
        else:
            balanced = True
            left = self.balanced_helper(root.left)
            right = self.balanced_helper(root.right)
            if (abs(left[0] - right[0]) > 1):
                balanced = False
            return (max([left[0], right[0]]) + 1, left[1] and right[1] and balanced)
        
