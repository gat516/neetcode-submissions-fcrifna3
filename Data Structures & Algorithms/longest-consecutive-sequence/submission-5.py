class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: given an array of integers
        #consecutive sequence of elements do not have to be consecutive in the array.
        
        num_set = set(nums)
        longestSequence = 0

        #is this number a start or not?
        for num in nums:
            if(num - 1) not in num_set:
                length = 0
                while(num + length) in num_set:
                    length  += 1
                longestSequence = max(longestSequence, length)

        return longestSequence
