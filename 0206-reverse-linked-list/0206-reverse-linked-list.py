# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute

        # temp = head
        # stack = []
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        
        # temp = head
        # while stack:
        #     ele = stack.pop()
        #     temp.val = ele
        #     temp = temp.next
        # return head

        # Optimal interative

        # prev = None
        # temp = head
        # while temp:
        #     front = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = front
        # return prev
        
        # Optimal recursive

        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head
        