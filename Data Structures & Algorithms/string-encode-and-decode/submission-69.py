class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "salt" + word

        return encoded_string



    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 1

        while r < len(s):

            word_length = ""
            while s[l].isnumeric():
                word_length += s[l]
                l += 1
            if word_length:
                word_length = int(word_length)
            else:
                return None
            
            l += 4
            r = l + word_length

            res.append(s[l:r:1])

            l = r

        return res


            

        
        return word_length
            




