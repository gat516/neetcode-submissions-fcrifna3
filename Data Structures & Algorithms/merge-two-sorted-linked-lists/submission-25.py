# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeLists(list1head, list2head):

            if not list1head:
                return list2head
            if not list2head:
                return list1head

            if list1head.val > list2head.val:
                list2head.next = mergeLists(list1head, list2head.next)
                return list2head
            else:
                list1head.next = mergeLists(list1head.next, list2head)
                return list1head

        return mergeLists(list1, list2)

            
