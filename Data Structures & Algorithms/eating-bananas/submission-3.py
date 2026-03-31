        #input: piles = [1,2,3,4], h = 9

        #decide k, my rating speed. minimum.


        #take a pile, divide by k, thats the time it takes to eat a pile. sum this up for each array. then compare against h.
        #we'll call this pilesPerHourSum

        #minimum integer k. so whatever that number is should be less than h.

        

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        kLow = 1
        kHigh = max(piles)

        result = kHigh

        while kLow <= kHigh:
            mid = (kLow + kHigh) // 2
            pilesPerHourSum = 0
            for pile in piles:
                pilesPerHourSum += (pile + mid - 1) // mid

            if pilesPerHourSum <= h:
                result = mid
                kHigh = mid - 1
            else:
                kLow = mid+1

        return result