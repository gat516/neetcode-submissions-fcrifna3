from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        freqCounter = {}
        word1 = Counter(s)


        for i in range(0, len(s)):
            freqCounter[s[i]] = freqCounter.get(s[i], 0) + 1
            freqCounter[t[i]] = freqCounter.get(t[i], 0) - 1

        for val in freqCounter.values():
            if val != 0:
                return False
        
        return True

