class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = {}
        for c in s1:
            needs[c] = needs.get(c,0)+1
        size = len(s1)
        i = 0
        window = {}
        while i + size <= len(s2):
            part = s2[i:i+size]
            for c in part:
                window[c] = window.get(c,0)+1
            if window == needs:
                return True
            window.clear()
            i+=1
        return False