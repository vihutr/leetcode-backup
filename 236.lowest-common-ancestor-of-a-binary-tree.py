# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # preorder dfs:
        # naturally iterate through descendants of each node
        # preorder is simply a recursive call on the left then right
        if p == root or q == root or not root:
            return root
        # once p or q is found, recursively checks each branch that was past before finding the node for the remaining node,
        # to be stored in 'right'
        # by returning the given root when both left and right are found we get the lca when both are found,
        # while we retain the node to fulfill the condtion of being found by returning either whichever between left and right are found
        # to keep the information as we backtrack after our recrusive calls didn't find both nodes in their branch.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

# @leet end
