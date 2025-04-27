class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        l = r = result = 0
        maxF = -1
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if freq[s[r]] > maxF:
                maxF = freq[s[r]]
            
            while ((r-l) + 1) - maxF > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l+=1
            
            result = max(result ,((r-l) + 1))
            r+=1
        
        return result