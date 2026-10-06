import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        k = 0
        while l <= r:
            m = l + (r - l) // 2
            print(l, r, m)

            time = 0          
            for pile in piles:
                hourPerPile = math.ceil(pile / m)
                time += hourPerPile
            
            if time > h:
                l = m + 1
            elif time <= h:
                k = m
                r = m - 1
                

        return k
            
        
            
            


