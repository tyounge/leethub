# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        sz = 0
        while now != None:
            now = now.next
            sz += 1
        if sz == 1:
            return None
        now = head
        for i in range(sz//2 - 1):
            now = now.next
        now.next = now.next.next
        return head