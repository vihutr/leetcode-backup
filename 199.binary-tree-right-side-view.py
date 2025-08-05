# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # check if root
        if not root:
            return result
        # start queue with root
        queue = [root]

        # end search once no children left in a depth level; queue will be empty
        while len(queue) > 0:
            result.append(queue[-1].val)
            level_size = len(queue)
            for i in range(level_size):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        return result
# @leet end
