# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute

        # temp = head
        # mpp = defaultdict(int)
        # while (temp):
        #     if temp in mpp:
        #         return True
        #     mpp[temp] += 1
        #     temp = temp.next
        # return False

        # Optimal

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
