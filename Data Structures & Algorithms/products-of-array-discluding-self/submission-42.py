class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            prefix[i] = prefix[i] * suffix
            suffix =  nums[i] * suffix #how do we update suffix
        
        return prefix

        #1st pass: 8 * 8 = 48, suffix = 1
        #2nd pass: 2*

        #nums:   1,2,6,8
        #prefix: 1, 1, 2, 8
        #suffix: 1, 6, 24, 48

        #48, 24, 12, 8