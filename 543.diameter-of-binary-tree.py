# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get max length of left and right sides of every node
        # dfs recursive function while doing so (return max left and right)
        # keep track of max length found at anypoint b/c we only return max depth
        Solution.max_diameter = 0
        self.getMaxDepth(root)
        return Solution.max_diameter

    def getMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.getMaxDepth(root.left)
        right = self.getMaxDepth(root.right)
        diameter = left + right
        if Solution.max_diameter < diameter:
            Solution.max_diameter = diameter
        return max(left, right) + 1

# @leet end
