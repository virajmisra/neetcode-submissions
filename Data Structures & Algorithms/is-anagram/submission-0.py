class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = Counter(s)
        tm = Counter(t)
        return sm == tm

        