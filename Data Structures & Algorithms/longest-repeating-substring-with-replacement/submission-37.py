from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #when do i expand the window

        #when do i shrink it
        #if replacements exceed K

        l, r = 0, 0

        charMap = [0] * 26

        res = 0
        count = 0

        #invalid -> most frequent count + k is not enough
        #window size - most frequent count <= k

        while r < len(s):
            charMap[ord(s[r]) - ord('A')] += 1
            count += 1
            
            while (r - l + 1) - max(charMap) > k:
                charMap[ord(s[l]) - ord('A')] -= 1
                count -= 1
                l += 1


            res = max(count, res)

            r += 1
            
            


        return res