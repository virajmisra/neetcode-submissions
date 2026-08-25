from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = Counter(s1)
        l = 0
        r = len(s1)
        have = Counter(s2[l:r])
        while r < len(s2):
            if have == needs:
                return True
            have[s2[l]] -= 1 
            l += 1
            have[s2[r]] = have.get(s2[r],0) + 1
            r += 1
        return have == needs

        