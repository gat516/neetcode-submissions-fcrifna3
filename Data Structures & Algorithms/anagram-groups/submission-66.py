from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for word in strs:
            charMap = [0] * 26
            for c in word:
                charMap[ord(c) - ord('a')] += 1
            key = tuple(charMap)
            res[key].append(word)

        return list(res.values())