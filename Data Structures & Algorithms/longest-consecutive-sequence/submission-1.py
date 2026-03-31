#find the length of the longest consecutive sequence from the array
#the elements do not need to be adjacent, just consecutive in value
#O(n)
#return will be an integer that is the length of the problem


#empty list
#one number
#maybe negatives, but i dont think that really affects the algorithm

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set: #is this number a potential start?
                currentNumber = num
                sequenceCount = 1
                
                #while i have consecutive numbers,
                while currentNumber + 1 in num_set:
                    currentNumber += 1
                    sequenceCount += 1
                
                max_length= max(max_length, sequenceCount)

        return max_length
                    
        #for num in nums
            #if start of sequence:
                #count how long the sequence extends
                #track the maximum length found so far
        
