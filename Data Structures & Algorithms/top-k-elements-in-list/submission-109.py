import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        buckets = [[] for _ in range(len(nums) + 1)]

        #counter array

        frequencyMap = Counter(nums)

        for value, frequency in frequencyMap.items():
            buckets[frequency].append(value)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i]) - 1, -1, -1):
                result.append(buckets[i][j])
                
                if len(result) == k:
                    return result

        