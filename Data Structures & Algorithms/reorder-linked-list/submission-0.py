# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second :
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        a , b = head , prev
        while b :
            tmp1 , tmp2 = a.next , b.next
            a.next = b
            b.next = tmp1
            a , b = tmp1 , tmp2
        
        