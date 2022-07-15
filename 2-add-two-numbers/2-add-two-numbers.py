# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        answer = ListNode()
        now = answer
        while l1 != None or l2 != None:
            y = x
            if l1 != None:
                y += l1.val
                l1 = l1.next
            if l2 != None:
                y += l2.val
                l2 = l2.next
            now.next = ListNode(val = y%10)
            x = y//10
            now = now.next
        if x != 0:
            now.next = ListNode(val = x)
        return answer.next