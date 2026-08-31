class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l, r = 0, 1
        if not s:
            return 0

        seen = set(s[l])

        count = 1
        maxcount = 1

        while r < len(s):

            #if it's a dupe, reset
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
            else:
                seen.add(s[r])
                count += 1
                maxcount = max(count, maxcount)
                r += 1

        return maxcount
