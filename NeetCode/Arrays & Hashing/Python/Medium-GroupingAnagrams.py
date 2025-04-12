# Time Complexity: O(n * m log m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key not in diction:
                diction[key] = []
            diction[key].append(word)
        
        return list(diction.values())

# Important lesson: Don't forget that dictionaries can hold lists!
# I originally tried having the key,value pair be unsorted, sorted.
# This broke for identical works and empty strings. Having it be
# sorted,[anagrams] works perfectly!

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         diction = {}

#         for i in strs:
#             diction[i] = "".join(sorted(i))
#         newSet = set(diction.values())
        
#         result = []
#         for i in newSet:
#             temp = []
#             for x in diction:
#                 print(x)
#                 if diction[x] == i:
#                     temp.append(x)
#             result.append(temp)
#         return result