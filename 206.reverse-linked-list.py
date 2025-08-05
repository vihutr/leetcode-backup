# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # deal with edge cases immediately
        if not head:
            return None
        if not head.next:
            return head
        # use 2 main pointers and a temp pointer in the loop to reverse the list in O(n)
        prev = head
        curr = head.next
        prev.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
# @leet end
