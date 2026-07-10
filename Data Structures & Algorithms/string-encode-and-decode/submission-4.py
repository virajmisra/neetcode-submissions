class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res = res + str(l) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < (len(s)):
            j = i
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + length + 1
        return res
