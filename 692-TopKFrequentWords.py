# Time Complexity: O(n log n) due to sorted().
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        emptyDict = {}

        for i in words:
            if i in emptyDict.keys():
                emptyDict[i] += 1
            else:
                emptyDict[i] = 1

        # Instead of using reverse, we make the values negative. It still sorts from min to max,
        # but since the values are negative, it correctly orders the keys!
        sorted_dict = dict(sorted(emptyDict.items(), key=lambda item: (-item[1], item[0])))        
        most_frequent_values = list(sorted_dict)[:k]
        return most_frequent_values
