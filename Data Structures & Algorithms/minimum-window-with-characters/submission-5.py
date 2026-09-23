class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        l = 0
        r = 0
        have = 0
        need = len(tMap)
        minLength = float('inf')
        res = ""

        window = {}

        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1

            while have >= need:
                res = s[l:r+1] if minLength > (r+1) - l else res
                minLength = min(minLength,(r+1)-l)


                window[s[l]]-=1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return res



        