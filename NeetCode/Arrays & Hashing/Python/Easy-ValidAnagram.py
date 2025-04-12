class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}

        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i] += 1
        
        for i in t:
            if i in dictS:
                dictS[i] -= 1
                continue
            return False

        for i in dictS.values():
            if i != 0:
                return False
        
        return True
