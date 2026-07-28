#Input: strs = ["act","pots","tops","cat","stop","hat"]
#Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            charMap = [0] * 26

            for c in word:
                charMap[ord(c) - ord('a')] += 1
            
            charMap = tuple(charMap)
            result[charMap].append(word)

        
        return list(result.values())