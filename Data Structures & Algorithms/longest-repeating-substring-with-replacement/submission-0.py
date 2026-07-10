class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            c = s[r]
            counts[c] = counts.get(c,0)+1
            mostFreq = max(counts.values())
            while sum(counts.values()) - mostFreq > k:
                counts[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
        