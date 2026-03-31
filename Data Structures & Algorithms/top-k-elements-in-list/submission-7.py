class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k number of most frequent elements

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        heap = []
        for key, count in freq.items():
            heapq.heappush(heap, (count, key))
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        return [key for count, key in heap] # "key for count" = unpacks, "key in heap" means to return only heap
        