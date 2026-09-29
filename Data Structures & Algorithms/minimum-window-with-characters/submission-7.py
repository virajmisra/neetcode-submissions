class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        l = 0
        r = 0 
        haves = 0
        needs = len(tMap)

        minL = float('inf')
        res = ""

        window = {}
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in tMap and window[s[r]] == tMap[s[r]]:

                haves += 1
                while haves == needs:
                    res = s[l:r+1] if minL > r+1 - l else res
                    minL = min(minL, r+1 - l)

                    if s[l] in tMap and window[s[l]] == tMap[s[l]]:
                        haves -= 1
                    window[s[l]] -= 1
                    l += 1
            r += 1
        return res
        