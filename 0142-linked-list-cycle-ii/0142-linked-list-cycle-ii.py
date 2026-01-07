# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        mpp = {}
        while temp:
            if temp in mpp:
                return temp
            mpp[temp] = 1
            temp = temp.next
        return None
        