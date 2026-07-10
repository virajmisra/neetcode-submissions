class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of most frequent character in window
        # if window size - most frequent <= k, its a valid window

        l = 0
        r = 0
        counts = {}
        res = 0
        mostFreq = 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r],0)+1
            mostFreq = max(mostFreq, max(counts.values()))
            if (r - l + 1) - mostFreq <= k:
                res = max(res,(r-l+1))
            else:
                while l < r and (r - l + 1) - mostFreq > k:
                    counts[s[l]] -= 1
                    l += 1
            r +=1
        return res
