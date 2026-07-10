class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c,0) + 1
        need = len(tMap)
        have = 0
        l = 0
        r = 0
        res = ""
        minLength = float('inf')
        window = {}
        while r < len(s):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in tMap and window[s[r]]==tMap[s[r]]:
                have += 1
            while have == need:
                if (r-l+1 < minLength):
                    res = s[l:r+1]
                    minLength = r-l+1
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return res