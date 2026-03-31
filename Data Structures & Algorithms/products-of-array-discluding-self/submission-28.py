class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = 1

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            print(prefix[i])

        for i in range(len(nums) - 1, -1, -1):
            res[i] = suffix * prefix[i]
            suffix = suffix * nums[i]
            print("i: ", i, ": ",suffix)

        print(suffix)

        return res