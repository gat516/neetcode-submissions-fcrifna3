# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fastptr = head
        slowptr = head

        while fastptr is not None and fastptr.next is not None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if slowptr == fastptr:
                return True
        return False      