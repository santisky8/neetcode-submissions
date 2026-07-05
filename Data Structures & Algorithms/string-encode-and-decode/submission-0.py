class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # For each word, attach its length, a '#', and ther word itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # The pointer to go through the encoded string

        while i < len(s):
            j = i
            # Find where the '#' is for this specific word segment
            while s[j] != '#':
                j += 1

            # The character between i and j form the length of the word
            length = int(s[i:j])

            # Extract the word using slicing
            # Starts after teh '#' and ends after the character length 
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move pointer 'i' to the start of the next encoded word block
            i = j + 1 + length

        return res
