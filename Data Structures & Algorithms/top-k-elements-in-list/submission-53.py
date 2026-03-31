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
                print("popping.. ", freq[num, " "])
                heapq.heappop(res)
        
        result = []
        for f, n in res:
            result.append(n)
        return result