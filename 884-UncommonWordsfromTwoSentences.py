#Time Complexity: O(n + m), where n is the length of s1 and m is the length of s2
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        diction = {}
        result = []

        # For each word in each sentence, add it to a dictionary. If it isn't already in the dictionary, add it and make the value 0. If it is already in the dictionary, increment the value by 1.
        for i in words1:
            if i in diction:
                diction[i] += 1
                continue
            diction[i] = 0
        
        for i in words2:
            if i in diction:
                diction[i] += 1
                continue
            diction[i] = 0
#Find all values with a value of 0
        for key in diction:
            if diction[key] == 0:
                result.append(key)
        return result