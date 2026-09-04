from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            freqMap = [0] * 26
            for c in word:
                freqMap[ord(c) - ord('a')] += 1

            key = tuple(freqMap)

            res[key].append(word)

        return list(res.values())
