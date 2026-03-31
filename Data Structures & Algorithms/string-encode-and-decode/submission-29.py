class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" +  word

        return encoded_string


    def decode(self, s: str) -> List[str]:
        
        decoded_string = []

        i = 0
        j = 0
        
        while i < len(s):
            wordLength = ""

            while(s[i] != '#' and s[i].isnumeric()):
                wordLength += s[i]
                i+=1
            wordLength = int(wordLength)
            
            j = i+1
            decoded_string.append(s[j:j + wordLength:1])
            i = j + wordLength

        return decoded_string
