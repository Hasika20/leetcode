# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute

        # stack = []
        # temp = head
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        # temp = head
        # while temp:
        #     if temp.val != stack.pop():
        #         return False
        #     temp = temp.next
        # return True

        # Optimal

        # slow = head
        # fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # prev = None
        # curr = slow.next
        # while curr:
        #     front = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = front
        # temp = head
        # while prev:
        #     if temp.val != prev.val:
        #         return False
        #     temp = temp.next
        #     prev = prev.next
        # return True

        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        low = 0
        high = n - 1
        while low < high:
            if arr[low] != arr[high]:
                return False
            low += 1
            high -= 1
        return True
        
        


        