class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1

        largest_area = 0


        while l < r:

            width = r - l
            area = 0
            if heights[l] < heights[r] and l < r:
                area = width * heights[l]
                l += 1
            elif heights[l] > heights[r] and l < r:
                area = width * heights[r]
                r -= 1
            elif heights[l] == heights[r] and l < r:
                area = width * heights[r]
                l += 1

            largest_area = max(area, largest_area)

        return largest_area
            