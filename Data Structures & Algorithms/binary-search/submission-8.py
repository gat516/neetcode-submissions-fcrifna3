class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        #[1,2,3,4,5,6]
        while left <= right:
            middle = (left+right) //2 
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                return middle
        return -1
