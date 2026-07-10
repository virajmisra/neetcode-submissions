class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        s1Sorted = "".join(sorted(s1))
        i = 0
        while i + size <= len(s2):
            window = "".join(sorted(s2[i:i+size]))
            if window == s1Sorted:
                return True
            i+=1
        return False