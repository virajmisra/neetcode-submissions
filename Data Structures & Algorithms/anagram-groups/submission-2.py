class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in d.keys():
                d[key].append(s)
            else:
                d[key] = []
                d[key].append(s)
        res = []
        for l in d.keys():
            res.append(d[l])
        return res