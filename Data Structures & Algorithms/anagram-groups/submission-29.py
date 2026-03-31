from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for word in strs:
            charFreq = [0] * 26
            for c in word:
                charFreq[(ord(c) - ord('a'))]+= 1
            charFreq = tuple(charFreq)

            res[charFreq].append(word)
        return  list(res.values())
            
            