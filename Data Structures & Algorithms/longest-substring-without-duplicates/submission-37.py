class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest_substring = 0


        l, r = 0, 1

        if len(s) == 1:
            return 1
        elif len(s) > 1:
            seen[s[0]] = 0

        while r < len(s):
            print(l, " : ", r)
            if s[r] in seen:
                l = max(l ,seen[s[r]] + 1)
                seen[s[r]] = r
            else:
                seen[s[r]] = r
            current_substring = r - l + 1
            longest_substring = max(current_substring, longest_substring)
            r+= 1
        
        return longest_substring
            