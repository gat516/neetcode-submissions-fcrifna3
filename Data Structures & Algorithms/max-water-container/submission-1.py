class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0


        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            if area < height * width:
                area = height * width
                if heights[l] >= heights[r]:
                    r -= 1
                else:
                    l += 1
            
            elif heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return area
        