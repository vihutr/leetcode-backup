# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        queue = []
        queue.append(head.val)
        ptr = head
        while ptr.next:
            ptr = ptr.next
            queue.append(ptr.val)
        for i in range(len(queue)):
            if queue[len(queue)-i-1] == 1:
                calc = 2 ** i
                result += calc
        return result
# @leet end
