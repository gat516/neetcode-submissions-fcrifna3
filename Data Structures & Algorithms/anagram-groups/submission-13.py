from collections import OrderedDict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            count = tuple(count)
            results[count].append(word)
        return list(results.values())
