# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #traverse to half
        cut = None
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #reverse 2nd half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #now merge 1st and 2nd half
        curr1, curr2 = head, prev
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next

            curr1.next = curr2
            curr2.next = tmp1        

            curr1 = tmp1
            curr2 = tmp2

        



