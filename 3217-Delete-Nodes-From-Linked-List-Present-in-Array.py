# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Since we are using Python, we do not need to worry about memory leaks because of Python's garbage collector.
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Move until the first valid node. The numbers in the nums lists are the numbers that we want to remove. Iterate through the linkedlist so that the head does not start on an invalid node.
        while head and head.val in nums:
            head = head.next
      
        if head is None: return None

        # Move forward, former prev value is deleted by python garbage collector.
        prev = head
        curr = head.next
        
        while curr is not None:
            #if value is not being removed, set prev and next to be updated
            if curr.val not in nums:
                prev.next = curr
                prev = curr
            #if the value IS being removed, we don't update the prev and prev.next values, meaning that the specific value we want removed will be removed.
            curr = curr.next
        # Remove any lingering issues
        prev.next = None
        return head