class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqCounter = {}

        s = s.lower()
        t = t.lower()

        for i in range(len(s)):
            freqCounter[s[i]] = freqCounter.get(s[i], 0) + 1
            freqCounter[t[i]] = freqCounter.get(t[i], 0) - 1
        
        for v in freqCounter.values():
            if v != 0:
                return False
        
        return True