# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS of each level, so use a queue
        res = []
        curr_lvl = []
        queue = deque([])
        # add nodes of each level th
        if root:
            res.append([root.val])
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        print('start queue loop')
        while queue:
            curr_q_size = len(queue)
            for i in range(curr_q_size):
                n = queue.popleft()
                print(n.val)
                curr_lvl.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            res.append(curr_lvl)
            curr_lvl = []
        print(res)
        return res

# @leet end
