class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i,v in enumerate(nums): #loop through nums
            diff = target - v #check difference for each num
            if diff in differences: #if diff is foundx
                return [differences[diff], i]
            differences[v] = i
            