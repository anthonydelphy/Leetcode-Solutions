# Optimal solution using Bucket Sort
# Time Complexity = O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for  i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)

        result = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

# Initial Solution. Time Complexity = O(nlogn)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         diction = {}

#         for i in nums:
#             if i not in diction:
#                 diction[i] = 1
#                 continue

#             diction[i] += 1

#         result = []
#         sorted_list = sorted(diction.items(), key=lambda item: item[1], reverse=True)
#         for i in range(k):
#             result.append(sorted_list[i][0])
#         return result