class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        needs = len(tMap)
        have = 0
        res = ""
        minL = float("inf")

        l = 0
        r = 0
        window = {}
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1

                while have >= needs:
                    if minL > r+1-l:
                        minL = r+1-l
                        res = s[l:r+1]

                    window[s[l]] -= 1
                    if s[l] in tMap and tMap[s[l]] > window[s[l]]:
                        have -= 1
                    l += 1
            r += 1
        return res





