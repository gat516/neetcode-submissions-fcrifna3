class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #

        #input: -1, 0, 1, 2, -1, -4
        #have to find sets that equal to 0
        # [[-1 + -1 + 2 = 0], [-1 +0 + 1 = 0]]

        nums = sorted(nums)


        l = 0 
        r = len(nums) - 1


        result = []

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                target = -(nums[l] + nums[r])

                if nums[i] == target:
                    result.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[i] < target:
                    l += 1
                elif nums[i] > target:
                    r -= 1
        
        return result
                            
            

        