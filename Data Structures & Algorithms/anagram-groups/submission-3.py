class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        res = []
        for s in strs:
            ss = str(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)
        for s in d:
            res.append(d[s])
        return res
        