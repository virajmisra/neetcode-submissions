class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        chars = set()
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            res = max(res,len(chars))
            r+=1
        return res