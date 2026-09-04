class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums = sorted(nums)

        l, r = 0, len(nums) - 1

        res = []

        for i in range(0, len(nums) - 1):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                
        return res
        
            
            