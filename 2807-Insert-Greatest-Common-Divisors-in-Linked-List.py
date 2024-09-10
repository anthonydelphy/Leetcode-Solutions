# This is my own personal solution to the Daily Problem of September 10th, 2024.

# Time Complexity: O(n)

# Possible Improvements: While this solution is in O(n) time complexity, it still iterates through the LinkedList twice. This code could be improved by iterating through the list once and placing the values in while iterating.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    #This is how the math library in python solves greatest commmon factors. 
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head

        # Edgecase: One digit:
        if head.next is None:
            return head

        # Create a list of additions to linked list, each seperated by one value
        while temp.next:
            lst.append(gcd(temp.val, temp.next.val))
            temp = temp.next

        print('List of factors: ', lst)

        temp = head #reset list
        nextVal = lst.pop(0)

        while head.next:
            rightSection = head.next
            head.next = ListNode(nextVal, rightSection)
            if len(lst) > 0:
                nextVal = lst.pop(0)
            head = head.next.next

        head = temp
        return head



        