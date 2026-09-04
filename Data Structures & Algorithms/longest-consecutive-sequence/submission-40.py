class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest_count = 0
        count = 0

        hashmap = set(nums)

        for num in nums:
            #start
            if num - 1 not in hashmap:
                i = 0
                count = 0
                while num + i in hashmap:
                    print(num + i)
                    count += 1
                    highest_count = max(count, highest_count)
                    i += 1




        return highest_count

        #1 not in nums ,count = 0. 3 in nums, count += 1.