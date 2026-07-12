class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charMap = [0] * 26

        if len(s) != len(t):
            return False

        charMap = [0] * 26

        for i in range(len(s)):
            charMap[(ord(s[i]) - ord('a'))] += 1
            charMap[(ord(t[i]) - ord('a'))] -= 1

        return charMap == [0] * 26
