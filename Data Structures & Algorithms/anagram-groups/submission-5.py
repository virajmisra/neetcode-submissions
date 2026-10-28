class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = str(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)
        res = []
        for l in d.values():
            res.append(l)
        return res
        