class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqcounter = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freqcounter[ord(s[i]) - ord('a')] -= 1
            freqcounter[ord(t[i]) - ord('a')] += 1

        allzero = True
        for v in freqcounter:
            if v != 0:
                allzero = False
        return allzero