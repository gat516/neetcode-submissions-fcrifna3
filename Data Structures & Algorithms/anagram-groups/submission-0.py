class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for string in strs:
            letterfreq = [0] * 26
            for c in string:
                letterfreq[ord(c) - ord('a')] += 1
            key = tuple(letterfreq)
            output[key].append(string)

        print(output)
        return list(output.values())
