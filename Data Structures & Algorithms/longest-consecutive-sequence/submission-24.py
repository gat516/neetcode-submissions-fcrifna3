class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest_count = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                count = 1

                while num + count in nums:
                    count += 1

                highest_count = max(count, highest_count)


        return highest_count

        #1 not in nums ,count = 0. 3 in nums, count += 1.