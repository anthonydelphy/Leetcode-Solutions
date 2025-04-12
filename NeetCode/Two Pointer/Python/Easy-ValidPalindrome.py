# My own solution. Time Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = []
        s = s.lower()
        for i in s:
            if ord('a') <= ord(i) and ord(i) <= ord ('z'):
                sList.append(i)
            if ord('0') <= ord(i) and ord(i) <= ord ('9'):
                sList.append(i)


        l,r = 0, len(sList) -1
        while l <= r:
            if sList[l] != sList[r]:
                return False
            l += 1
            r -= 1

        return True
    
#Alternative Solution from Neetcode
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l,r = 0, len(s)-1

#         while l < r:
#             while l < r and not self.alphaNum(s[l]):
#                 l+=1
#             while r > l and not self.alphaNum(s[r]):
#                 r -= 1
            
#             if s[l].lower() != s[r].lower():
#                 return False
#             l,r = l+1,r-1
#         return True


#     def alphaNum(self, s):
#         return (ord('A') <= ord(s) <= ord('Z') or
#         ord('a') <= ord(s) <= ord('z') or
#         ord('0') <= ord(s) <= ord('9'))