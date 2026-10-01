class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        

        while left <= right:
            mid = left + ((right - left) // 2)

            #if it's the drop:
            if nums[mid] < nums[mid - 1]:
                return nums[mid]                
            elif nums[mid] > nums[right]: #minimum is somewhere to the right
                left = mid + 1

            elif nums[mid] < nums[right]: #minimum is somewhere to the left
                right = mid - 1

            elif nums[mid] == nums[right]:
                return nums[mid]

        return nums[mid]
        

                