# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyptr = ListNode(0,head)
        curr = dummyptr
        k = dummyptr
        for i in range(n):
            k = k.next
        while k.next:
            curr = curr.next
            k = k.next

        curr.next = curr.next.next
        return dummyptr.next