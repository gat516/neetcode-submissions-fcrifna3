from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Step 1: Create an output array to hold prefix products
        output = [1] * n

        # Step 2: Fill prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]  # update prefix for next index

        # Step 3: Multiply by suffix products (from right to left)
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]  # update suffix for next index

        return output
