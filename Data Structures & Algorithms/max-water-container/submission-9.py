class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        largest_area = 0


        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            largest_area = max(area, largest_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                r -= 1

        return largest_area