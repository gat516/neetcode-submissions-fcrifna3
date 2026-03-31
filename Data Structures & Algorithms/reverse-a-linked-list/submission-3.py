# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next #ok, so store temporary next
            curr.next = prev #change the lnik from forward to reverse
            prev = curr #move prev to curr
            curr = nxt #move curr to curr next
        return prev