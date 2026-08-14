class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = [[] for _ in range(len(nums) + 1)]

        #do a pass that loops and create a dictionary to frequency. count all the freqs



        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for num, frequency in freq_map.items():
            frequencies[frequency].append(num)

        result = []

        for freq in range(len(frequencies) -1, 0, -1):
            for num in frequencies[freq]:
                result.append(num)

                if len(result)==k:
                    return result
