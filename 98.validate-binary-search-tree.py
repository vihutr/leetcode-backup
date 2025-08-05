# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs recursion?
        vals = []
        self.inorderTraversal(root, vals)
        # print(vals)
        for i in range(len(vals) - 1):
            if vals[i] >= vals[i + 1]:
                return False
        return True

    def inorderTraversal(self, root, out):
        if root:
            self.inorderTraversal(root.left, out)
            out.append(root.val)
            self.inorderTraversal(root.right, out)
# @leet end
