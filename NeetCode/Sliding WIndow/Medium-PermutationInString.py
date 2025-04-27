class Solution(object):
    def checkInclusion(self, s1, s2):

        count, s1Len = Counter(s1), len(s1)   
        for i in range(len(s2)):
            if s2[i] in count: 
                count[s2[i]] -= 1

            if i >= s1Len and s2[i-s1Len] in count: 
                count[s2[i-s1Len]] += 1

            if all([count[i] == 0 for i in count]):
                return True

        return False