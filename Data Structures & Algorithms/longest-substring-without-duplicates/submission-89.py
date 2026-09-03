class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0

        count = 0
        max_count = 0

        seen = set()

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                count -= 1

            seen.add(s[r])
            count += 1
            max_count = max(max_count, count)
            r += 1

        return max_count
        
