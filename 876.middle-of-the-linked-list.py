# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one iterates by 1, the other iterates by 2
        # because we want the second middle node given 2 middles:
        # we just wait for when the fast iterator sees .next=None,
        # if we iterate the slow iterator first we get to the 2nd middle node
        if not head:
            return None
        if not head.next:
            return head
        by1 = head
        by2 = head
        while by2.next is not None:
            by1 = by1.next
            by2 = by2.next
            if by2.next:
                by2 = by2.next
        return by1
# @leet end
