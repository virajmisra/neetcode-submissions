class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        res = ""
        minL = float("inf")
        tMap = Counter(t)
        window = {}

        have = 0
        need = len(tMap)
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1

                while have >= need:
                    if minL > (r+1) - l:
                        res = s[l:r+1]
                        minL = r+1 - l
                    
                    if s[l] in tMap and window[s[l]] == tMap[s[l]]:
                        have -= 1
                    window[s[l]] -= 1
                    l += 1
            r += 1

        return res
                    