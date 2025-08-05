# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        return nav(head, visited)

def nav(node, visited):
    if not node:
        return False
    if node.val in visited:
        if node in visited[node.val]:
            return True
        visited[node.val].append(node)
    else:
        visited[node.val] = [node]
    return nav(node.next, visited)
# @leet end
