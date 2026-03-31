import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        print(freq)
        
        for num in freq:
            heapq.heappush(res, (freq[num], num))
            if(len(res) > k):
                heapq.heappop(res)
        return [num for freq, num in res]