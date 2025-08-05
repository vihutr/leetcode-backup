# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = fun(root)
        # print(res)
        # -1 used as 'Unbalanced' flag due to 0 being equivalent to False in python
        return res != -1

def fun(root):
    if root:
        print(f'val: {root.val}')
        l = fun(root.left)
        if l == -1:
            # print(f'not l: {l}')
            return -1
        r = fun(root.right)
        if r == -1:
            # print(f'not r: {r}')
            return -1
        # check for when difference is too high to return as unbalanced
        diff = abs(l - r)
        if diff > 1:
            # print(f'imbalance detected at: {root.val}')
            return -1
        # get height at any given node, adding 1 at each "return" to the parent
        # the height to be passed along is the max subtree height
        return max(l, r) + 1
    else:
        # when getting to end of a tree path, 0 height start point
        return 0
        

# @leet end
