# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#2, 4, 6, 8, 10
#2, 10, 4, 8, 6

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #this part of the algorithm finds the halfpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half of list
        halfPoint = slow.next #halfpoint is after slow.,next
        prev = None #split the list
        slow.next = None #split the list
        while halfPoint:
            tmp = halfPoint.next
            halfPoint.next = prev
            prev = halfPoint
            halfPoint = tmp

        #right now, halfPoint is at tail.next
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
