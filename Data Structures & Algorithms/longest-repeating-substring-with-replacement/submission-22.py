#replace up to k letters to get longest possible substring.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l,r = 0, 0
        freq = {}
        max_freq = 0
        longest_replacement = 0


        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            print(freq)
        
            if freq[s[r]] > max_freq:
                max_freq = freq[s[r]]
            
            
            window_length = r - l + 1
            print("l: ", l, " r: ", r)
            print("window length: ", window_length, "longest replacement: ", longest_replacement,)

            if window_length - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            else:
                longest_replacement = max(window_length, longest_replacement)
                
            r += 1

        return longest_replacement

            
            