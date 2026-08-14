class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "salt"
            encoded_string += word

        return encoded_string
    


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        
        read, write = 0, 1

        while write < len(s):
            length = ""
            while s[read].isnumeric():
                length += s[read]
                read += 1

                if s[read+1:read+4:1] == "salt":
                    break
            if length:
                length = int(length)
                read = read + 4 #skip the salt
                write = read + length
                decoded_string.append(s[read:write:1])
                read=write
                write=read

#5salthello5saltworld


        return decoded_string



