class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        charMap = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            charMap[ord(s[i]) - ord('a')] += 1
            charMap[ord(t[i]) - ord('a')] -= 1

        for freq in charMap:
            if freq != 0:
                return False
        
        return True
