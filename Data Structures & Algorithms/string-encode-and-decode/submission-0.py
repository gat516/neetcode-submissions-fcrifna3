class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])).zfill(4) + strs[i]
            output += strs[i]
        return output
    
    def decode(self, s: str) -> List[str]:
        output = []
        while s:
            length = int(s[0:4:1]) #grabs the 4 digit id, converting to int
            s = s[4::1] #slices 4 digit id, getting rid of the id

            output.append(s[:length:1])
            s = s[length::1]
        return output
